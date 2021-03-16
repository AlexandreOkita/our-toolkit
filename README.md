# Our ToolKit - Python3 Library
Open source python library focused on learning about how to contribute to open source process and sharing some "useless" and funny functions

![our-toolkit](https://i.kym-cdn.com/entries/icons/original/000/034/467/Communist_Bugs_Bunny_Banner.jpg)

## How to contribute

### First Step - Forking the Repository:

Fork this repository and clone your new forked repository to your machine. 

To fork the repository you will find a button written `fork` on the top of this page. To clone your forked repo, click on the green button written `Code` and copy the https url (if you wish you can also use ssh to clone it). The link will be something like: `https://github.com/YOUR-USERNAME/our-toolkit.git`.

### Second Step - Push your contribution:

Now it's time to make your contribution! But before doing it, create a new branch and checkout to it using the following command: `git checkout -b [BRANCH-NAME]`. Usually the branch name gives the idea of what you want to implement in the code.

You can check several different ways of how to contribute in [this file](CONTRIBUTING.md) ! (Do not forget to add your name in [Contributors.md](Contributors.md) 😉

Once you have made your contribution, **it's time to commit it!**

Run the following commands:

- `git status` - this will show you all your modifications 
- `git add [FILE]` - this will stage the modified file. You can add all modified files in a directory using `git add .`
- `git commit -m "[MESSAGE]"` - this command will create your commit! Create it with a short description (usually under 50 characters) of your changes
- `git push origin [YOUR-BRANCH-NAME]` - this command will send your modifications to your github forked repository

### Third Step - Create your PR:

Once you pushed your commit, you will see a `Compare & pull request` green button on the top of your forked repo page (if you don't see it, create the PR clicking on the Pull Requests button).

Confirm in the top of the page, if you are merging to the original repository in `base fork`.

Now, you can write a good title to your PR that indicates the changes you did, and explain them better on the comment section. Click on `Create Pull Request` and you are done! Now just wait some reviewer check your code, and soon it will be available for everyone!


