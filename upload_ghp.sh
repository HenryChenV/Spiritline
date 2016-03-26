#!/bin/bash

BASE_DIR=`pwd`
OUTPUT_DIR=${BASE_DIR}/output
TMP_DIR=${BASE_DIR}/tmp
GHP_REPO_URL=git@github.com:HenryChenV/henrychenv.github.io.git
GHP_SITE_URL=henrychenv.github.io
PERSONAL_BLOG_URL=spiritline.threebook.cn
PUBLISHCONF=publishconf.py
BACKUP_SUFFIX=".bak"
GHP_PUB_MSG="Published From Pelican."
REPO_DIR=${TMP_DIR}/${GHP_SITE_URL}


sed -i"${BACKUP_SUFFIX}" "s/${PERSONAL_BLOG_URL}/${GHP_SITE_URL}/g" ${PUBLISHCONF}
make publish

#rm -rf ${TMP_DIR}
mkdir -p ${TMP_DIR}

if [ -e ${REPO_DIR}/.git ]; then
    echo PULL
    cd ${REPO_DIR}
    git pull
else
    echo CLONE
    cd ${TMP_DIR}
    git clone ${GHP_REPO_URL}
fi

cd ${REPO_DIR}
git rm -rf * > /dev/null
cp -r ${OUTPUT_DIR}/* ${REPO_DIR}/
git add .
git commit -m ${GHP_REPO_URL}
git push

cd ${BASE_DIR}

#rm -rf ${TMP_DIR}

mv ${BASE_DIR}/${PUBLISHCONF}${BACKUP_SUFFIX} ${BASE_DIR}/${PUBLISHCONF}
