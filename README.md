# keysafe.software



#### Attention: from now you can run this project only on Raspberry Pi


## Settings for display resolution from Waveshare 10.1inch HDMI LCD (H)
As first you need update your configuration file for correct display resolution.
To edit the configuration file, see the instructions at [R-Pi_ConfigurationFile.](http://elinux.org/R-Pi_configuration_file)
```
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
```
## Clone into your home 'eval echo ~$USER' directory
```
git clone https://github.com/VolVoz/keysafe.software.git
```

## For Debian/Raspbian/Ubuntu

```
sudo apt-get update
sudo apt-get install python-qt4 pyqt4-dev-tools qt4-designer
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils

```

## Install PostgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev
```

#### Install requirements
```
sudo pip install --upgrade pip
sudo pip install -r requirements/requirements.txt
```

#### Create database and user from psql

1. Login as default user: sudo -i -u postgres
2. Create new User: createuser --interactive
3. When prompted for role name, enter linux username, and select Yes to superuser question.
4. Still logged in as postgres user, create a database: createdb <username_from_step_3>
5. Confirm error(s) are gone by entering: psql at the command prompt.
6. Output should show psql (x.x.x) Type "help" for help.
7. Run from terminal ./makedb.sh
8. Run python keysafe.software/database.createdb.py


#### Check created database:
```
psql -d cad_keysafe
cad_keysafe=# \dt

             List of relations
             
| Schema |     Name      | Type  |  Owner   |
|--------|---------------|-------|----------|
| public | key           | table | cad_root |
| public | key_places    | table | cad_root |
| public | user          | table | cad_root |
| public | user_key_link | table | cad_root |

(4 rows)

```

## Install PyQt on OS X (for development)
```
$ brew install pyqt
```

### TODO:

- [x] Create requirements for Linux system
- [x] Create simple UI design
- [x] Connect windows
- [x] Folder structure
- [x] Setup Database
- [X] Setup RFID reader
- [X] Make a runner
