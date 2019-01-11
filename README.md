# PhyG


## Français

Écran de bienvenue qui lie différents sous programmes servant à visualiser des phénomènes physiques vus dans des cours de niveau Cégep (système d'éducation québécois).  Les différents phénomènes sont :

* [Onde sonore stationnaire](https://github.com/Pattedetable/onde-sonore-stationnaire)

* [Interférence et diffraction](https://github.com/Pattedetable/interference-diffraction)

Le fichier utilisé pour démarrer l'écran de bienvenue est ```PhyG.py```.

Pour les différentes dépendances de chaque sous-programme, référez-vous à leur page respective.

À ce stade du développement, ces sous-programmes doivent être dans le même répertoire que l'écran de bienvenue.


### Utilisation

Afin d'utiliser ce programme, vous aurez besoin des logiciels suivants :

  * Python 3

Si vous utilisez Linux, Python sera généralement déjà installé.  Si ce n'est pas déjà fait, vous pouvez installer Python 3 à partir des dépôts de logiciels de votre distribution.

Que vous utilisiez Linux, MacOS ou Windows, vous pouvez aussi installer Python à partir du [site officiel](https://www.python.org/).  Sélectionnez ensuite le paquet correspondant à votre système d'exploitation.

Vous aurez aussi besoin des modules Python suivants :

  * PyQt5

Si vous utilisez Linux, il est fort probable qu'ils se trouvent dans les dépôts logiciels de votre distribution.

Pour tous les systèmes d'exploitation supportés, à partir de la version 3.4, Python inclus de plus `pip`, un gestionnaire de paquet qui permet d'installer des modules pour Python.  Pour vérifer la version de Python installée sur votre système, ouvrez un terminal (Linux, MacOS) ou une invite de commande (Windows) et tappez :

```python --version```

Si le numéro de version affiché à l'écran commence par 2, dans tout ce qui suit, utilisez `python3` au lieu de `python`, et `pip3` au lieu de `pip`.

Vous pouvez vous servir de `pip` pour installer les divers modules nécessaires.  Par exemple, pour installer PyQt5 sur Linux, une fois les droits administrateurs obtenus, entrez dans un terminal :

```python pip install PyQt5```

Sur Windows, vous n'avez pas besoin des droits administrateurs, et la commande est plutôt :

```pip install PyQt5```

Une fois ces modules installés, dans le terminal sous Linux et MacOS ou l'invite de commande sous Windows, entrez :

```python PhyG.py```

Sous Windows, vous pouvez aussi double-cliquer sur le fichier ```PhyG.py```.


### License

Le programme est distribué sous la licence GNU GPLv3.  Pour le texte complet, référez-vous au fichier `LICENSE`.
La version courte de cette licence est que vous êtes libre d'utiliser ce logiciel, d'en modifier le code source, ainsi que de le redistribuer, que ce soit sous sa version originale ou modifiée.  Cependant, vous devez donner ces mêmes droits aux personnes qui utiliseront votre logiciel redistribué.

Le code source est disponible sur [GitHub](https://github.com/Pattedetable/ecran-bienvenue-physique).

Ce logiciel utilise des bibliothèques du projet FFmpeg sous la licence LGPLv2.1, de Qt sous la licence LGPLv3, ainsi que de Python, Numpy et Matplotlib.


## English

Welcome screen linking together various programs each illustrating a physical phenomenon covered at the Cégep level in Québec's education system.  The different phenomena are:

* [Standing sound wave](https://github.com/Pattedetable/onde-sonore-stationnaire)

* [Interference and diffraction](https://github.com/Pattedetable/interference-diffraction)

The file used to start the program is ```PhyG.py```.

For the dependancies needed by each program, please refer to its page.

At this point in development, those programs must be in the same directory as the welcome screen.


### Usage

You will need some software to use this program, namely:

  * Python 3

If you are using Linux, Python will generally already be installed.  If not, you can install it from your distribution's repositories.

You can also install Python from the [official website](https://www.python.org/).  Once there, select the appropriate package for your operating system.

You will also need the following Python modules:

  * PyQt5

On Linux, you will most likely find these modules in your distribution's repositories.

On all supported operating systems, starting with version 3.4, Python includes `pip`, a package manager for Python which can be used to install the necessary modules.  To check the version of Python that is installed on your system, open a terminal (Linux, MacOS) or a command prompt (Windows) and type in:

```python --version```

If the version number displayed on screen begins with 2, replace `python` with `python3` and `pip` with `pip3` in every command that follows.

You can then use `pip` to install the necessary modules.  For instance, to install PyQt5 on Linux, acquire administrator rights and then type in a terminal:

```python pip install PyQt5```

On Windows, administrator rights are not required, and the command is instead:

```pip install PyQt5```

Once these are installed, open a terminal on Linux or MacOS (or command prompt on Windows) and enter:

```python PhyG.py```

Moreover, on Windows, you can simply double-click on the ```PhyG.py``` file.


### License

This program is distributed under the GNU GPLv3 licence.  The details of this license can be found in the `LICENSE` file.
The short version is that you are free to use this software, to modify its source code, and to redistribute it in either its original or modified form.  However, you have to give those same rights to the users of the redistributed software.

The source code is available on [GitHub](https://github.com/Pattedetable/ecran-bienvenue-physique).

This software uses libraries from the FFmpeg project under the LGPLv2.1, Qt under the LGPLv3, Python, Numpy and Matplotlib.
