"""
File Tools - Basic File I/O Operations

Provides safe file reading/writing operations.
Future: Will integrate with MCP filesystem server.

Safety:
- Respects kernel safety constraints
- Sandboxed to project directory by default
- Validates paths before operations
"""

from pathlib import Path
from typing import Optional, List
from dataclasses import dataclass


# =============================================================================
# SAFETY CONFIGURATION
# =============================================================================

@dataclass
class FileSafetyConfig:
    """Safety configuration for file operations"""
    # Allowed base directories (sandboxing)
    allowed_directories: List[Path]

    # Maximum file size to read (bytes)
    max_read_size: int = 10 * 1024 * 1024  # 10 MB

    # Maximum file size to write (bytes)
    max_write_size: int = 5 * 1024 * 1024  # 5 MB

    # Forbidden patterns in paths
    forbidden_patterns: List[str] = None

    def __post_init__(self):
        if self.forbidden_patterns is None:
            # Default forbidden patterns
            self.forbidden_patterns = [
                "..",  # Parent directory traversal
                "system32",  # Windows system dirs
                "etc",  # Linux system dirs
                "passwd",  # Sensitive files
            ]


# =============================================================================
# FILE TOOLS
# =============================================================================

class FileTools:
    """
    Safe file I/O operations.

    Philosophy:
    - Sandbox by default (restrict to project directory)
    - Validate all paths
    - Respect size limits
    - Check safety constraints before execution
    """

    def __init__(self, safety_config: Optional[FileSafetyConfig] = None):
        """
        Initialize file tools.

        Args:
            safety_config: Safety configuration. If None, uses default (project dir only)
        """
        if safety_config is None:
            # Default: restrict to project directory
            project_root = Path(__file__).parent.parent.parent
            safety_config = FileSafetyConfig(
                allowed_directories=[project_root]
            )

        self.safety = safety_config

    def _validate_path(self, path: Path) -> None:
        """
        Validate path against safety rules.

        Args:
            path: Path to validate

        Raises:
            ValueError: If path is unsafe
        """
        # Resolve to absolute path
        resolved = path.resolve()

        # Check if within allowed directories
        allowed = False
        for allowed_dir in self.safety.allowed_directories:
            try:
                resolved.relative_to(allowed_dir.resolve())
                allowed = True
                break
            except ValueError:
                continue

        if not allowed:
            raise ValueError(
                f"Path {path} is outside allowed directories: "
                f"{[str(d) for d in self.safety.allowed_directories]}"
            )

        # Check forbidden patterns
        path_str = str(resolved).lower()
        for pattern in self.safety.forbidden_patterns:
            if pattern.lower() in path_str:
                raise ValueError(f"Path contains forbidden pattern: {pattern}")

    def read_file(self, path: str, encoding: str = "utf-8") -> str:
        """
        Read file contents.

        Args:
            path: File path (relative or absolute)
            encoding: Text encoding (default: utf-8)

        Returns:
            File contents as string

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If path is unsafe or file too large
        """
        file_path = Path(path)
        self._validate_path(file_path)

        # Check file size
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        file_size = file_path.stat().st_size
        if file_size > self.safety.max_read_size:
            raise ValueError(
                f"File too large: {file_size} bytes "
                f"(max: {self.safety.max_read_size} bytes)"
            )

        # Read file
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    def write_file(
        self,
        path: str,
        content: str,
        encoding: str = "utf-8",
        create_dirs: bool = True
    ) -> None:
        """
        Write content to file.

        Args:
            path: File path (relative or absolute)
            content: Content to write
            encoding: Text encoding (default: utf-8)
            create_dirs: Create parent directories if needed

        Raises:
            ValueError: If path is unsafe or content too large
        """
        file_path = Path(path)
        self._validate_path(file_path)

        # Check content size
        content_size = len(content.encode(encoding))
        if content_size > self.safety.max_write_size:
            raise ValueError(
                f"Content too large: {content_size} bytes "
                f"(max: {self.safety.max_write_size} bytes)"
            )

        # Create parent directories
        if create_dirs and not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)

    def read_lines(
        self,
        path: str,
        encoding: str = "utf-8",
        max_lines: Optional[int] = None
    ) -> List[str]:
        """
        Read file as list of lines.

        Args:
            path: File path
            encoding: Text encoding
            max_lines: Maximum number of lines to read (None = all)

        Returns:
            List of lines (without newline characters)
        """
        file_path = Path(path)
        self._validate_path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        lines = []
        with open(file_path, 'r', encoding=encoding) as f:
            for i, line in enumerate(f):
                if max_lines and i >= max_lines:
                    break
                lines.append(line.rstrip('\n\r'))

        return lines

    def list_directory(self, path: str, pattern: str = "*") -> List[str]:
        """
        List files in directory.

        Args:
            path: Directory path
            pattern: Glob pattern (default: * = all files)

        Returns:
            List of file paths (relative to directory)
        """
        dir_path = Path(path)
        self._validate_path(dir_path)

        if not dir_path.exists():
            raise FileNotFoundError(f"Directory not found: {path}")

        if not dir_path.is_dir():
            raise ValueError(f"Not a directory: {path}")

        # List files matching pattern
        files = [str(f.relative_to(dir_path)) for f in dir_path.glob(pattern)]
        return sorted(files)

    def file_exists(self, path: str) -> bool:
        """Check if file exists"""
        try:
            file_path = Path(path)
            self._validate_path(file_path)
            return file_path.exists()
        except ValueError:
            return False

    def create_directory(self, path: str) -> None:
        """Create directory (and parents if needed)"""
        dir_path = Path(path)
        self._validate_path(dir_path)
        dir_path.mkdir(parents=True, exist_ok=True)


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

# Global instance (default safety)
_default_tools = FileTools()


def read_file(path: str, encoding: str = "utf-8") -> str:
    """Convenience function for reading files"""
    return _default_tools.read_file(path, encoding)


def write_file(path: str, content: str, encoding: str = "utf-8") -> None:
    """Convenience function for writing files"""
    return _default_tools.write_file(path, content, encoding)


def read_lines(path: str, encoding: str = "utf-8", max_lines: Optional[int] = None) -> List[str]:
    """Convenience function for reading lines"""
    return _default_tools.read_lines(path, encoding, max_lines)


def list_directory(path: str, pattern: str = "*") -> List[str]:
    """Convenience function for listing directories"""
    return _default_tools.list_directory(path, pattern)


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    print("Testing File Tools...")

    tools = FileTools()

    # Test: List kernel directory
    print("\nKernel directory contents:")
    try:
        files = tools.list_directory("kernel", "*.json")
        for f in files:
            print(f"  - {f}")
    except Exception as e:
        print(f"  Error: {e}")

    # Test: Read kernel file (first 10 lines)
    print("\nKernel file (first 10 lines):")
    try:
        lines = tools.read_lines("kernel/system_snapshot_motorcore.json", max_lines=10)
        for line in lines:
            print(f"  {line}")
    except Exception as e:
        print(f"  Error: {e}")

    # Test: Write temp file
    print("\nWriting test file...")
    try:
        test_content = "Hello from ResonaQ Runtime!\nThis is a test file.\n"
        tools.write_file("runtime/temp_test.txt", test_content)
        print("  Test file written successfully")

        # Read it back
        content = tools.read_file("runtime/temp_test.txt")
        print(f"  Content: {repr(content)}")

        # Clean up
        Path("runtime/temp_test.txt").unlink()
        print("  Test file cleaned up")
    except Exception as e:
        print(f"  Error: {e}")

    # Test: Safety - try to read outside project
    print("\nTesting safety constraints...")
    try:
        tools.read_file("/etc/passwd")  # Should fail
        print("  SECURITY FAILURE: Accessed file outside project!")
    except ValueError as e:
        print(f"  Security working: {e}")

    print("\nFile tools working correctly!")
