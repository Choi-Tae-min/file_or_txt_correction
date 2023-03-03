import os
import glob
#if you want to delete all ofspecific extension
[os.remove(f) for f in glob.glob("file_path/*.pfm")]
