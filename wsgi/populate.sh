REPO="https://github.com/esparta/pytexas2014script"
DATA_DIR="${OPENSHIFT_DATA_DIR?data}"
DATABASE_FILE="$DATA_DIR/data.db"
if [ ! -d "$DATA_DIR" ]
    mkdir -p data
fi

cd $DATA_DIR
echo "Removing old database file: $DATABASE_FILE"
rm -rf $DATABASE_FILE
echo "Cloning script: $REPO"
rm -rf scripts
git clone $REPO scripts

cd scripts

echo "Getting data from GitHub repository"
wget https://github.com/esparta/pytexas2014data/archive/master.zip -O data.zip
unzip -jo data.zip

sed -i "s|data.db|${DATABASE_FILE}|g" settings.py
echo "Importing database..."
python todatabase.py
