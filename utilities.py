import os

def resetKnownFaces():
    pickleEmbedFile = "ref_embed.pkl"
    pickleNameFile = "ref_name.pkl"
    # If the pickle embed file exists, remove it and recreate it
    if (os.path.isfile(pickleEmbedFile)):
        os.remove(pickleEmbedFile)
    # If the pickle name file exists, remove it and create a new one
    if (os.path.isfile(pickleNameFile)):
        os.remove(pickleNameFile)
    open(pickleEmbedFile, 'w')
    open(pickleNameFile, 'w')

if __name__ == "__main__":
    resetKnownFaces()