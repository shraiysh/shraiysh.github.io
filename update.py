import subprocess
import tempfile
import os
import argparse

def init(commits_file):
    with open(commits_file, 'w') as f:
        f.write('''---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# LLVM Commits

This is an incomplete list of the LLVM Commits authored by me - 

''')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src_dir', help='The source directory of llvm project')

    args = parser.parse_args()
    commits_file =  os.path.join(os.getcwd(), 'commits.md')
    os.chdir(args.src_dir)
    subprocess.run(['git', 'pull'], capture_output=True)
    init(commits_file)
    p = subprocess.run(['git', '--no-pager', 'log', '--author', '\(Shraiysh\)\|\(shraiysh\)', '--pretty=oneline'], capture_output=True)
    for commit in p.stdout.decode().splitlines():
        commit_hash = commit.split()[0]
        commit_title = ' '.join(commit.split()[1:])
        with open(commits_file, 'a') as f:
            f.write(f' 1. [{commit_title}](https://github.com/llvm/llvm-project/commit/{commit_hash})\n')

if __name__ == '__main__':
    main()