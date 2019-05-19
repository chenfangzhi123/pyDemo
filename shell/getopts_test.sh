#!/bin/bash
while getopts :v: option
do
    case "$option" in
        v)
            version=$OPTARG;;
        \?|:)
            echo "非常参数：$OPTARG"
            echo "使用说明: [-v version] hosts_list"
            echo "-v 版本号（不加则忽略版本直接更新）"
            ;;
    esac
done
shift $(($OPTIND - 1))
files=$@
for file in $files ; do
    if [[  ! -f "$file" || ! -r "$file" ]]
    then
        echo "文件$file 不存在或者不可读！"
        exit 1
    fi
done


