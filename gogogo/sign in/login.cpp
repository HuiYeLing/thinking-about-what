#include<cstring>                   ///字符串函数
#include<iostream>                  ///输入输出流
using namespace std;

///——————————————————————登录系统结构体——————————————————————
struct sjk          ///最多可注册20个用户;
{
    ///主系统登录系统
    char zhanghao[100],mima[100];///账号、密码
    char name[100],zjh[100];///姓名、证件号
    int jifen,zz;///积分，是否实名认证以及权限标识
} sjk[30];

int i,n,m,s,p,q,k=0;
char linshizhanghao[100],linshimima[100];
int xiabiao;///n为主系统操作指令，m为用户操作指令
char panduan,formatting[100]= {'\0'},Admin[100]= {"Administrator"},Password[100]= {"Admin"};///判断y/n，格式化，管理员账号

int main()
{
    cout<<"1.注册 2.登陆 3.结束"<<endl;   ///0.后台检测代码
    while(1)
    {
        cout<<"请输入需要执行的操作：";
        cin>>n;
        if(n==1)            ///-注册;
        {
            if(k<20)
            {
                cout<<"账号：";
                cin>>sjk[k].zhanghao;
                cout<<"密码：";
                cin>>sjk[k].mima;
                p=0;
                for(i=0; i<k; i++)
                {
                    if(strcmp(sjk[i].zhanghao,sjk[k].zhanghao)==0)
                    {
                        p++;
                    }
                }
                if(p!=0)
                {
                    cout<<"此用户名已被注册!"<<endl;
                    strcpy(sjk[k].zhanghao,formatting);
                    strcpy(sjk[k].mima,formatting);
                }
                else
                {
                    cout<<"恭喜您成为第"<<k+1<<"位注册本系统的用户"<<endl;
                    sjk[k].jifen=0;     ///初始积分为0
                    sjk[k].zz=0;        ///初始未进行实名认证,游客权限
                    k++;
                }
            }
            else
                cout<<"用户已满！"<<endl;
        }
        if(n==2)            ///-登录（包括管理员账号）;
        {
            cout<<"账号：";
            cin>>linshizhanghao;
            cout<<"密码：";
            cin>>linshimima;
            p=0;
            xiabiao=0;
            if(strcmp(Admin,linshizhanghao)==0&&strcmp(Password,linshimima)==0)                ///管理员登录操作
            {
                strcpy(linshizhanghao,formatting);
                strcpy(linshimima,formatting);
                cout<<endl<<"————hello Administrator！————"<<endl<<endl;
                for(i=0; i<k; i++)
                {
                    cout<<"已注册的第"<<i+1<<"号用户"<<endl<<"账号:"<<sjk[i].zhanghao<<'\t'<<"密码:"<<sjk[i].mima<<'\t'<<"积分："<<sjk[i].jifen<<endl;
                    if(sjk[i].zz>=1)
                        cout<<"姓名："<<sjk[i].name<<'\t'<<"证件号："<<sjk[i].zjh<<endl;
                }
                cout<<endl<<"————hello Administrator！————"<<endl<<endl;
                cout<<"1.注销 2.退出管理员模式"<<endl<<"请输入要执行的管理员操作:";
                while(cin>>m)
                {
                    if(m==1)
                    {
                        cout<<"请输入需要注销的账号：";
                        cin>>linshizhanghao;
                        cout<<"密码：";
                        cin>>linshimima;
                        cout<<"请确认是否注销，一旦注销账号将无法找回 y/n"<<endl;
                        cin>>panduan;
                        if(panduan=='y')
                        {
                            ///从注册的用户中找到需要注销的账号进行注销
                            p=0;
                            xiabiao=0;
                            for(i=0; i<k; i++)
                            {
                                if(strcmp(sjk[i].zhanghao,linshizhanghao)==0&&strcmp(sjk[i].mima,linshimima)==0)
                                {
                                    p++;
                                }
                                if(p==1)
                                {
                                    xiabiao=i;
                                    p++;
                                }
                            }
                            p--;
                            if(p==1)
                            {
                                for(i=xiabiao; i<k; i++)
                                {
                                    strcpy(sjk[i].zhanghao,sjk[i+1].zhanghao);
                                    strcpy(sjk[i].mima,sjk[i+1].mima);
                                    sjk[i].jifen=sjk[i+1].jifen;
                                    strcpy(sjk[i+1].zhanghao,formatting);
                                    strcpy(sjk[i+1].mima,formatting);
                                    sjk[i+1].jifen=0;
                                }
                                k--;
                                cout<<xiabiao+1<<"号用户注销成功!"<<endl;
                            }
                            if(p!=1)
                                cout<<"账号或密码错误，无法注销！"<<endl;
                        }
                        if(panduan='n')
                            cout<<"取消注销"<<endl;
                    }
                    if(m==2)
                    {
                        cout<<endl<<"————Byebye Administrator！————"<<endl<<endl;
                        break;
                    }
                    cout<<"请输入要执行的管理员操作:";
                }
            }
            else                    ///普通用户登录操作
            {
                for(i=0; i<k; i++)
                {
                    if(strcmp(sjk[i].zhanghao,linshizhanghao)==0&&strcmp(sjk[i].mima,linshimima)==0)
                    {
                        p++;
                    }
                    if(p==1)
                    {
                        xiabiao=i;
                        p++;
                    }
                }
                p--;
                if(p==1)
                {
                    cout<<"第"<<xiabiao+1<<"位用户登陆成功!"<<endl<<"您目前的积分为:"<<sjk[xiabiao].jifen<<endl;
                    cout<<"您的权限为：";
                    if(sjk[xiabiao].zz==0)
                        cout<<"游客权限"<<'\t'<<"请及时进行实名认证，以免影响后续操作"<<endl;
                    if(sjk[xiabiao].zz==1)
                        cout<<"普通用户"<<endl;
                    if(sjk[xiabiao].zz==2)
                        cout<<"普通会员"<<endl;
                    cout<<"1.签到  2.充值  3.兑换  4.查询  5.改密  6.实名认证  7.关闭"<<endl;
                    cout<<"10.进入信鸽系统"<<endl;///子系统入口
                    cout<<"请输入要执行的用户操作：";
                    while(cin>>m)
                    {
                        if(m==1)
                        {
                            sjk[xiabiao].jifen+=10;
                            cout<<"签到成功，当前积分为："<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==2)
                        {
                            int money;
                            cout<<"请适度娱乐理性消费!"<<endl;
                            cout<<"输入任意金额：";
                            cin>>money;
                            sjk[xiabiao].jifen+=money;
                            cout<<"充值成功，当前积分为："<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==3)
                        {
                            cout<<"1.预习资料  10积分"<<endl<<"2.学习资料  10积分"<<endl<<"3.复习资料 10积分"<<endl<<"4.试卷一套  10积分"<<endl;
                            int l=0;
                            cout<<"请输入想要兑换的商品：";
                            cin>>l;
                            if(l>0&&l<5)
                            {
                                sjk[xiabiao].jifen-=10;
                                cout<<"恭喜您成为第一位幸运顾客，买一发四，您以获得全套学习资料"<<endl;
                                cout<<"剩余积分："<<sjk[xiabiao].jifen<<endl;
                            }
                        }
                        if(m==4)
                        {
                            cout<<"您的权限为：";
                            if(sjk[xiabiao].zz==0)
                                cout<<"游客权限"<<'\t'<<"请及时进行实名认证，以免影响后续操作"<<endl;
                            if(sjk[xiabiao].zz==1)
                                cout<<"普通用户"<<endl;
                            if(sjk[xiabiao].zz==2)
                                cout<<"普通会员"<<endl;
                            cout<<"您当前的积分为："<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==5)
                        {
                            char linshi[100];
                            cout<<"请输入原密码：";
                            cin>>linshi;
                            if(strcmp(sjk[xiabiao].mima,linshi)==0)
                            {
                                cout<<"原密码正确,请输入新密码：";
                                cin>>sjk[xiabiao].mima;
                                cout<<"修改成功！";
                            }
                            else
                                cout<<"原密码错误！"<<endl;
                        }
                        if(m==6)
                        {
                            cout<<"——————实名认证——————"<<endl;
                            cout<<"输入姓名：";
                            cin>>sjk[xiabiao].name;
                            cout<<"输入证件号：";
                            cin>>sjk[xiabiao].zjh;
                            cout<<"——————认证成功——————"<<endl;
                            cout<<"奖励积分+100"<<endl;
                            sjk[xiabiao].jifen+=100;
                            sjk[xiabiao].zz=1;
                        }
                        if(m==7)
                        {
                            cout<<"关闭！"<<endl;
                            break;
                        }
                        cout<<"请输入要执行的用户操作：";
                    }
                }
                else
                {
                    cout<<"账号或密码错误"<<endl;
                    strcpy(linshizhanghao,formatting);
                    strcpy(linshimima,formatting);
                }
            }
        }
        if(n==3)          ///-结束程序
        {
            cout<<"结束程序"<<endl;
            break;
        }
        if(n==0)            ///-后台监测代码;
        {
            for(i=0; i<25; i++)
            {
                cout<<"第"<<i+1<<"号用户"<<endl<<"账号:"<<sjk[i].zhanghao<<'\t'<<"密码:"<<sjk[i].mima<<'\t'<<"积分："<<sjk[i].jifen<<endl;
                cout<<"姓名："<<sjk[i].name<<'\t'<<"证件号："<<sjk[i].zjh<<endl;
            }
        }
    }
    return 0;
}

