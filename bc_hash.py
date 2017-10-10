import hashlib, json, sys

def hashMe(msg=""):
    #Helper function wrapping hasing algorithm
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)   # Sort keys to guarantee repeatability

    if sys.version_info.major ==2:
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
