学习笔记
1.MySql的安装：
    1.获取安装包
        wget http://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz
    2.解压
        tar -xzvf mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz
    3.移动到/use/local/
        mv mysql-5.7.17-linux-glibc2.5-x86_64 /usr/local/mysql
    4.进入/usr/local/mysql目录下,创建一个为mysql的用户
        groupadd mysql
    　　  useradd -g mysql mysql
    5.创建mysql数据仓库目录
        mkdir /data/mysql
    6.改变目录所属者
        cd /usr/local/mysql
        pwd
        chown -R mysql .
        chgrp -R mysql .
        chown -R mysql /data/mysql
    7.配置参数
        bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/data/mysql
            注意：此处可能遇到错误
                error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory
            解决：
                sudo apt-get install libaio-dev
                再次执行配置参数的命令即可，注意生成的随机密码@localhost: qekqri-ec3fR
        bin/mysql_ssl_rsa_setup  --datadir=/data/mysql
    8.修改系统配置文件
        cd /usr/local/mysql/support-files
        cp my-default.cnf /etc/my.cnf
        cp mysql.server /etc/init.d/mysqld

        vim /etc/init.d/mysql
            修改内容：
                basedir=/usr/local/mysql
                datadir=/data/mysql
    9.启动mysql
        /etc/init.d/mysql start
    以上可能会出问题

采用这个方案：
    Ubuntu下安装mysql:
        sudo apt-get install mysql-server
        sudo apt install mysql-client
        sudo apt install libmysqlclient-dev
        进入数据库：
            mysql -uroot -p
        启动数据库：
            service mysql start
        查看数据库是否启动：
            ps -ef | grep mysqld
2.mysql数据库的操作：
    创建数据库：
        create DATEBASE 数据库名;
    查看所有数据库：
        show databases;
    使用数据库：
        use test;  # test为数据库名，进入到test数据库
        表的使用：
            show tables;


遇到的问题：
1.数据库插入字符时字符乱码问题：
    在创建表时制定字符编码即可, 'ENGINE=InnoDB DEFAULT CHARSET=utf8'
2.数据库的cursor能不能在多次获取关闭，有什么影响？
3.只有cur.close()之后才能conn.commit()吗？顺序会有什么影响？
