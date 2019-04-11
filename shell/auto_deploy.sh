#!/usr/bin/env bash

# 高亮打印机器部署结果
warn(){
    echo -e "\033[32;49;1m $* \033[0m"
}

# 参数说明
# $1 ip
function update(){
    warn "---->>>>>总数：$total 当前：$i 开始处理 ${ARR[0]} ip: ${ARR[1]}"
    result=0
    while [[ "$result" != "200"  ]]
    do
        port=`ssh  supertool@$1  "echo \\\$AUCTION_HOME|cut -c 43-46 "`
        # 判断版本号，如果版本号不够新直接更新，如果版本号比当前的新则需要用户介入时候决定执行当前的机器执行
        # 如果服务会启动py会报错
        cur_version=`curl -s "http://$1:$port/version" | python -c "import sys, json; print json.load(sys.stdin)['git.commit.id']"`

        if [[  -z "$version" ]]
        then
             version="defatult"
        fi
        if [[ "$cur_version" == "$version" ]];then
            warn "$1 已经是最新版本 跳过<<<<<---------"
            break
        fi

        # 运行部署脚本
        ssh -tt supertool@$1  "cd \$AUCTION_HOME/bin;nohup bash restart.sh &>/dev/null;sleep 3 "

        # 运行测试脚本
        ssh supertool@$1  "bash \$AUCTION_HOME/bin/auto_test.sh"

        # 执行查看状态脚本
        result=`ssh supertool@$1  "bash \\\$AUCTION_HOME/bin/test.sh |head -n 1|awk '{print \\\$2}'"`

        if [[ "$result" != "200" ]];
        then
            # 如果成功继续执行下一个机器如果不成功需要用户介入是否继续执行
            while [[ "$try" != "y" && "$try" != "n" ]]
            do
                read -p "是否重试(y/n)：" try
            done
            if [[ "$try" == "n" ]]; then
                warn "跳过：$1<<<<<---------"
                # 清除变量，不然会进入死循环
                unset try
                break
            else
                warn "重试：$1"
                unset try
            fi
        else
            warn "执行成功：$1<<<<<---------"
            break
        fi
    done
}
while getopts :v: option
do
    case "$option" in
        v)
            version=$OPTARG
            echo "更新版本号：$version";;
        \?|:)
            echo "非法参数：$OPTARG"
            echo "使用说明: [-v version] hosts_list"
            echo "-v 版本号（不加则忽略版本直接更新）"
            exit 1;;
    esac
done
shift $(($OPTIND - 1))

files=$@
#校验主机名文件是否存在
for file in ${files} ; do
    if [[  ! -f "$file" || ! -r "$file" ]]
    then
        echo "文件$file 不存在或者不可读！"
        exit 1
    fi
done

for file in ${files} ; do
    total=`cat ${file}|wc -l`
    declare -i i=0;

    IFS_BAK=$IFS
    IFS=$'\n'
    for host in `cat ${file}`
    do
        i=i+1;
        IFS=$IFS_BAK
        ARR=($host)
        IFS=$'\n'
        update ${ARR[1]}  ${ARR[2]}
    done
    IFS=$IFS_BAK
done




