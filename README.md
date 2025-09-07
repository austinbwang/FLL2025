<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center" style="padding: 0; margin: 0;">
  <a href="https://github.com/austinbwang/FLL2025">
    <img src="images/logo.png" alt="Team Pokemon" height="230">
  </a>
  <h3 style="color:#dd5a44;font-size:30px;font-weight:780">Team Pokemon</h3>
  <p>
    An awesome Lego Prime Spike projects
    <br />
  </p>
</div>

<!-- GETTING STARTED -->
## Getting Started

This is a step-by-step guide detailing how to establish a local development environment, configure it, and deploy Python code to Prime Hub.

### Prerequisites

The following list include everything you need to continue the Setup.
* GIT

    Download and intall from https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

* github.com account

    Sign up account: https://github.com/

    Keep your username and password, you will need it for local git command to access remote repositories over https.

* Python

    https://www.python.org/downloads/

    brew install python3

* VS Code

    Download and intall from https://code.visualstudio.com/download



### Setup Local Development Env

#### 1. Clone the repo

   ```sh
   cd {directory/for/saving/your/pokemon/project}
   git clone https://github.com/Aspenbw/PokemonFLL2024.git
   ```
   provide the username and password to clone

  Or

  Clone by SSH (recommended)

   ```sh
   cd {directory/for/saving/your/pokemon/project}
   git clone git@github.com:Aspenbw/PokemonFLL2023.git
   ```

  Follow the instruction:
  - [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

  - [Adding your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

  - [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

#### 2. Setup VS Code

##### 2.1  Open the Command Palette (`⇧⌘P`), search for the Python: Create Environment command, and select `Venv`

##### 2.2  The command presents a list of interpreters that can be used as a base for the new virtual environment, please select `Python 3.1x.x`.

##### 2.3  To use the virtual environment, open the command pallette again and search for `py create term` and select Python: Create Terminal.

##### 2.4  Installing required packages

- required packages and the Pylance extension ([offical link](https://pybricks.com/projects/tutorials/dev/tools/vscode/#installing-python-and-the-pylance-extension))

Install the pybricks, pybricksdev and other required package in the virtual environment (make sure you are in the virtual environment (.venv prompt)):
`````shell
pip3 install -r requirements.txt
# pip install pybricks
# pip install pybricksdev
`````

- Then follow the link above or search for `Pylance`` in the Extensions in VS Code and click Install to install the Pylance extension.


##### 2.5  Running programs ([offical link](https://pybricks.com/projects/tutorials/dev/tools/vscode/#downloading-and-running-programs))

- For Powered up hubs, you must use the pybricksdev command line tool instead.

- Run the following command (replacing my_program with the actual name of the program you want to run).
`````shell
pybricksdev run ble main.py
`````
- If you have more than one active hub, you can specify a specific hub by name:

`````shell
pybricksdev run ble --name "AspenBot" main.py
````````






<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Coding with Pybricks

## Formating with black
`````shell
black src
````````







<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

<!-- Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<!-- Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!-->

* [Team Tornado FLL Tracker: Superpowered](https://coda.io/d/Tornado-2023_d9vY0DHbz5U/About-Tornado_suO00#_luXc_)
* [Pybricks Documentation](https://docs.pybricks.com/en/latest/)
* [Pybricks Code online IDE](https://code.pybricks.com/)
* [Pybricks Code Beta (3.3.x)](https://beta.pybricks.com/)
* [Pybricks Source Code](https://github.com/pybricks)

* [Pybricks 3.3 examples](https://github.com/FLL-Team-24277/Master-Program-Fall-2023)
* [PYTHON PROGRAMMING LESSONS](https://primelessons.org/en/PyLessons.html)
* [Spike IDE online](https://spike.legoeducation.com/#/prime/project)
* [Spike Prime API doc online](https://sanjay.seshan.org/spikeprime-tools/spike.html)
* [Lego Hub API online](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/index.html)
* [Advanced Functions](https://github.com/azzieg/mindstorms-inventor/tree/main/word_blocks)

* [Lego PID — The Ultimate Line Follower](https://medium.com/kidstronics/lego-pid-the-ultimate-line-follower-45d4e517572b)


<p align="right">(<a href="#readme-top">back to top</a>)</p> 

