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
