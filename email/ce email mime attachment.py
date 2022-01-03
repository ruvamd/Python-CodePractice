import os.path
attachment_path='/python/ca.png'
attachment_filename=os.path.basename(attachment_path)
import mimetypes
mime_type,_=mimetypes.guess_type(attachment_path)
mime_type,mime_subtype=mime_type.split('/',1)

print(mime_type)
print(mime_subtype)
