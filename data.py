# Encoded By PyEncryptor
# A Product Of (SMR-MILON)
# https://github.com/SMRmilon01 

import marshal
import base64
import zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
