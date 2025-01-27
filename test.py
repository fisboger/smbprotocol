import uuid
import logging
import sys

from smbprotocol.connection import Connection
from smbprotocol.create_contexts import CreateContextName, \
    SMB2CreateContextRequest, SMB2CreateQueryMaximalAccessRequest
from smbprotocol.security_descriptor import AccessAllowedAce, AccessMask, \
    AclPacket, SDControl, SIDPacket, SMB2CreateSDBuffer
from smbprotocol.session import Session
from smbprotocol.structure import FlagField
from smbprotocol.open import CreateDisposition, CreateOptions, \
    FileAttributes, FilePipePrinterAccessMask, ImpersonationLevel, Open, \
    ShareAccess
from smbprotocol.tree import TreeConnect

logging.basicConfig(level=logging.ERROR)


server = sys.argv[1]

print("Testing server: " + server)
port = 445

connection = Connection(uuid.uuid4(), server, port)
connection.connect()

connection.disconnect(True)