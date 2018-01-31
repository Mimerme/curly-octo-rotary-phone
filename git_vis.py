import os

#Parse some basic information about the repository

try:
    os.chdir("./.git")
except FileNotFoundError:
    print("This directory is not a git repository")


with open("description", "r") as description_file:
    print("Description:\n" +  description_file.read())

print("Branches:")
git_branches = os.listdir("./refs/heads")
for branch in git_branches:
    print(branch)

print("\nRemotes:")
git_remotes = os.listdir("./refs/remotes")
for remote in git_remotes:
    print(remote)

print("\nTags:")
git_tags = os.listdir("./refs/tags")
for tag in git_tags:
    print(tag)


with open("HEAD", "r") as head_file:
    print("\nCurrent Branch:\n" +  head_file.read().replace("ref: ", ""))

#Parse the objects with zlib
import zlib

#Enumerate the roots of the branches

#Branches and their corresponding trees
branches = {}
print("Enumeration of the branches...")

heads = os.getcwd() + "/refs/heads/"
files = os.listdir(heads)
for file in files:
    with open(heads + file, "r") as head:
        #Splice off the newline
        line = head.read()
        branches[file] = line[:len(line)-1]

print branches
print " "

blobs = {}
commits = {}
tags = {}
trees = {}

print("Enumeration of objects")

#Enumerate the object files
object_path = os.getcwd() + "/objects/"
dirs = os.listdir(object_path)

for dir in dirs:
    if os.path.isfile(dir) == True:
        continue

    files = os.listdir(object_path + dir)
    for file in files:
        #TODO: Optomize by splitting the dirs?
        sha1_hash = dir + file

        #Expand the content with zlib
        with open(object_path + dir + "/" + file) as obj:
            content = zlib.decompress(obj.read())
            type = content[:5]

            if type == "commi":
                commits[sha1_hash] = content
            elif type == "blob ":
                blobs[sha1_hash] = content
            elif type == "tree ":
                trees[sha1_hash] = content
            elif type == "tag   ":
                tags[sha1_hash] = content
            else:
                print "Unidentified type : " + type

print "Blobs"
print blobs.keys()
print "Commits"
print commits.keys()
print "Trees"
print trees.keys()
print "Tags"
print tags.keys()

#Begin repo generation
