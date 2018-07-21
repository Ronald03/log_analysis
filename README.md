# DB Log Analysis
This python code connects with a database and adquires useful information about articles and authors, and finally exports it to a file.

## Install
 - Download python from [here](https://www.python.org/)
 - Fork and clone this repository [here](https://github.com/Ronald03/log_analysis)
 
## Requirements
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Download this pre-configure vagrant environment from [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip)

## Set environment
- Unzip the pre-configure vagrant environment on a desired directory
- From a terminal navigate the unziped directory and locate the `Vagrantfile` file under the `Vagrant` folder
- Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
-  Place database on the `vagrant` folder; this is a common folder beteween the Virtual machine and the host machine
- Bring the virtual machine back online (with `vagrant up`)
- Then log into it with `vagrant ssh`.
- To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`
- Finally place the `log_analysis.py` from this project on the `Vagrant` directory

## How to run
Once the Database has been loaded on the virtual machine, if not logged on already, log to the virtual mechine from a terminal using the command `vagrant ssh`. 

Navigate to the `Vagrant` directory by typing `cd /vagrant` and from here execute the python file by typing `python log_analysis.py`.

Once the machine completes the execution, look for the `art_report.txt` file on the `vagrant` directory containing the final result of the report.

### Notes
> If you need or want to modify the source file and result of this project, just open the `log-analysis.py` file from a text editor and modify it as you need.
> No VIEWS were required to get the information from the database; every result has been accomplished with one query 

## License
This is .....**free to the public!**
