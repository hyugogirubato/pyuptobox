import gzip
import struct
import time
from enum import Enum
from io import BytesIO


class OPERATING_SYSTEM(Enum):
    FAT = 0x00  # FAT filesystem (MS-DOS, OS/2, NT/Win32)
    AMIGA = 0x01  # Amiga
    VMS = 0x02  # VMS (or OpenVMS)
    UNIX = 0x03  # Unix
    VM_CMS = 0x04  # VM/CMS
    ATARI_TOS = 0x05  # Atari TOS
    HDFS = 0x06  # HPFS filesystem (OS/2, NT)
    MACINTOSH = 0x07  # Macintosh
    Z_SYSTEM = 0x08  # Z-System
    CP_M = 0x09  # CP/M
    TOPS_20 = 0x0A  # TOPS-20
    NTFS = 0x0B  # NTFS filesystem (NT)
    QDOS = 0x0C  # QDOS
    ACORN_RISCOS = 0x0D  # Acorn RISCOS
    UNKNOWN = 0xFF  # Unknown


class FLAG(Enum):
    FTEXT = 0x00  # Indicates that the file is ASCII text
    FHCRC = 0x01  # Indicates that a CRC16 checksum for the gzip header is present
    FEXTRA = 0x02  # Indicates that extra fields are present
    FNAME = 0x04  # Indicates that a filename is present
    FCOMMENT = 0x08  # Indicates that a comment is present


def compress(
        value: bytes,
        level: int = 9,
        timestamp: int = -1,
        extra_flags: FLAG = FLAG.FTEXT,
        operating_system: OPERATING_SYSTEM = OPERATING_SYSTEM.FAT
) -> bytes:
    if timestamp < 0:
        timestamp = time.time()

    gzip_header = bytearray()
    gzip_header.extend(b'\x1f\x8b\x08\x00')  # gzip magic header and compression method
    gzip_header.extend(struct.pack("<L", round(timestamp)))  # modification time (set to 0 for no timestamp)
    gzip_header.extend(struct.pack(">B", extra_flags.value))  # extra flags (set to 0x00 for ASCII text)
    gzip_header.extend(struct.pack(">B", operating_system.value))  # operating system (set to 0x00 for FAT filesystem)
    return bytes(gzip_header) + gzip.compress(value, compresslevel=level)[10:]


def decompress(value: bytes) -> bytes:
    return gzip.decompress(value)


def get_compression_level(value: bytes) -> int:
    bytes_io = BytesIO(value)
    with gzip.open(bytes_io, "rb") as gzip_file:
        gzip_header = gzip_file.read(10)
        compression_level = gzip_header[8] & 0x0F
    bytes_io.close()
    return compression_level
