#include<cstring>                   ///�ַ�������
#include<iostream>                  ///���������
using namespace std;

///����������������������������������������������¼ϵͳ�ṹ�塪������������������������������������������
struct sjk          ///����ע��20���û�;
{
    ///��ϵͳ��¼ϵͳ
    char zhanghao[100],mima[100];///�˺š�����
    char name[100],zjh[100];///������֤����
    int jifen,zz;///���֣��Ƿ�ʵ����֤�Լ�Ȩ�ޱ�ʶ
} sjk[30];

int i,n,m,s,p,q,k=0;
char linshizhanghao[100],linshimima[100];
int xiabiao;///nΪ��ϵͳ����ָ�mΪ�û�����ָ��
char panduan,formatting[100]= {'\0'},Admin[100]= {"Administrator"},Password[100]= {"Admin"};///�ж�y/n����ʽ��������Ա�˺�

int main()
{
    cout<<"1.ע�� 2.��½ 3.����"<<endl;   ///0.��̨������
    while(1)
    {
        cout<<"��������Ҫִ�еĲ�����";
        cin>>n;
        if(n==1)            ///-ע��;
        {
            if(k<20)
            {
                cout<<"�˺ţ�";
                cin>>sjk[k].zhanghao;
                cout<<"���룺";
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
                    cout<<"���û����ѱ�ע��!"<<endl;
                    strcpy(sjk[k].zhanghao,formatting);
                    strcpy(sjk[k].mima,formatting);
                }
                else
                {
                    cout<<"��ϲ����Ϊ��"<<k+1<<"λע�᱾ϵͳ���û�"<<endl;
                    sjk[k].jifen=0;     ///��ʼ����Ϊ0
                    sjk[k].zz=0;        ///��ʼδ����ʵ����֤,�ο�Ȩ��
                    k++;
                }
            }
            else
                cout<<"�û�������"<<endl;
        }
        if(n==2)            ///-��¼����������Ա�˺ţ�;
        {
            cout<<"�˺ţ�";
            cin>>linshizhanghao;
            cout<<"���룺";
            cin>>linshimima;
            p=0;
            xiabiao=0;
            if(strcmp(Admin,linshizhanghao)==0&&strcmp(Password,linshimima)==0)                ///����Ա��¼����
            {
                strcpy(linshizhanghao,formatting);
                strcpy(linshimima,formatting);
                cout<<endl<<"��������hello Administrator����������"<<endl<<endl;
                for(i=0; i<k; i++)
                {
                    cout<<"��ע��ĵ�"<<i+1<<"���û�"<<endl<<"�˺�:"<<sjk[i].zhanghao<<'\t'<<"����:"<<sjk[i].mima<<'\t'<<"���֣�"<<sjk[i].jifen<<endl;
                    if(sjk[i].zz>=1)
                        cout<<"������"<<sjk[i].name<<'\t'<<"֤���ţ�"<<sjk[i].zjh<<endl;
                }
                cout<<endl<<"��������hello Administrator����������"<<endl<<endl;
                cout<<"1.ע�� 2.�˳�����Աģʽ"<<endl<<"������Ҫִ�еĹ���Ա����:";
                while(cin>>m)
                {
                    if(m==1)
                    {
                        cout<<"��������Ҫע�����˺ţ�";
                        cin>>linshizhanghao;
                        cout<<"���룺";
                        cin>>linshimima;
                        cout<<"��ȷ���Ƿ�ע����һ��ע���˺Ž��޷��һ� y/n"<<endl;
                        cin>>panduan;
                        if(panduan=='y')
                        {
                            ///��ע����û����ҵ���Ҫע�����˺Ž���ע��
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
                                cout<<xiabiao+1<<"���û�ע���ɹ�!"<<endl;
                            }
                            if(p!=1)
                                cout<<"�˺Ż���������޷�ע����"<<endl;
                        }
                        if(panduan='n')
                            cout<<"ȡ��ע��"<<endl;
                    }
                    if(m==2)
                    {
                        cout<<endl<<"��������Byebye Administrator����������"<<endl<<endl;
                        break;
                    }
                    cout<<"������Ҫִ�еĹ���Ա����:";
                }
            }
            else                    ///��ͨ�û���¼����
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
                    cout<<"��"<<xiabiao+1<<"λ�û���½�ɹ�!"<<endl<<"��Ŀǰ�Ļ���Ϊ:"<<sjk[xiabiao].jifen<<endl;
                    cout<<"����Ȩ��Ϊ��";
                    if(sjk[xiabiao].zz==0)
                        cout<<"�ο�Ȩ��"<<'\t'<<"�뼰ʱ����ʵ����֤������Ӱ���������"<<endl;
                    if(sjk[xiabiao].zz==1)
                        cout<<"��ͨ�û�"<<endl;
                    if(sjk[xiabiao].zz==2)
                        cout<<"��ͨ��Ա"<<endl;
                    cout<<"1.ǩ��  2.��ֵ  3.�һ�  4.��ѯ  5.����  6.ʵ����֤  7.�ر�"<<endl;
                    cout<<"10.�����Ÿ�ϵͳ"<<endl;///��ϵͳ���
                    cout<<"������Ҫִ�е��û�������";
                    while(cin>>m)
                    {
                        if(m==1)
                        {
                            sjk[xiabiao].jifen+=10;
                            cout<<"ǩ���ɹ�����ǰ����Ϊ��"<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==2)
                        {
                            int money;
                            cout<<"���ʶ�������������!"<<endl;
                            cout<<"���������";
                            cin>>money;
                            sjk[xiabiao].jifen+=money;
                            cout<<"��ֵ�ɹ�����ǰ����Ϊ��"<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==3)
                        {
                            cout<<"1.Ԥϰ����  10����"<<endl<<"2.ѧϰ����  10����"<<endl<<"3.��ϰ���� 10����"<<endl<<"4.�Ծ�һ��  10����"<<endl;
                            int l=0;
                            cout<<"��������Ҫ�һ�����Ʒ��";
                            cin>>l;
                            if(l>0&&l<5)
                            {
                                sjk[xiabiao].jifen-=10;
                                cout<<"��ϲ����Ϊ��һλ���˹˿ͣ���һ���ģ����Ի��ȫ��ѧϰ����"<<endl;
                                cout<<"ʣ����֣�"<<sjk[xiabiao].jifen<<endl;
                            }
                        }
                        if(m==4)
                        {
                            cout<<"����Ȩ��Ϊ��";
                            if(sjk[xiabiao].zz==0)
                                cout<<"�ο�Ȩ��"<<'\t'<<"�뼰ʱ����ʵ����֤������Ӱ���������"<<endl;
                            if(sjk[xiabiao].zz==1)
                                cout<<"��ͨ�û�"<<endl;
                            if(sjk[xiabiao].zz==2)
                                cout<<"��ͨ��Ա"<<endl;
                            cout<<"����ǰ�Ļ���Ϊ��"<<sjk[xiabiao].jifen<<endl;
                        }
                        if(m==5)
                        {
                            char linshi[100];
                            cout<<"������ԭ���룺";
                            cin>>linshi;
                            if(strcmp(sjk[xiabiao].mima,linshi)==0)
                            {
                                cout<<"ԭ������ȷ,�����������룺";
                                cin>>sjk[xiabiao].mima;
                                cout<<"�޸ĳɹ���";
                            }
                            else
                                cout<<"ԭ�������"<<endl;
                        }
                        if(m==6)
                        {
                            cout<<"������������ʵ����֤������������"<<endl;
                            cout<<"����������";
                            cin>>sjk[xiabiao].name;
                            cout<<"����֤���ţ�";
                            cin>>sjk[xiabiao].zjh;
                            cout<<"��������������֤�ɹ�������������"<<endl;
                            cout<<"��������+100"<<endl;
                            sjk[xiabiao].jifen+=100;
                            sjk[xiabiao].zz=1;
                        }
                        if(m==7)
                        {
                            cout<<"�رգ�"<<endl;
                            break;
                        }
                        cout<<"������Ҫִ�е��û�������";
                    }
                }
                else
                {
                    cout<<"�˺Ż��������"<<endl;
                    strcpy(linshizhanghao,formatting);
                    strcpy(linshimima,formatting);
                }
            }
        }
        if(n==3)          ///-��������
        {
            cout<<"��������"<<endl;
            break;
        }
        if(n==0)            ///-��̨������;
        {
            for(i=0; i<25; i++)
            {
                cout<<"��"<<i+1<<"���û�"<<endl<<"�˺�:"<<sjk[i].zhanghao<<'\t'<<"����:"<<sjk[i].mima<<'\t'<<"���֣�"<<sjk[i].jifen<<endl;
                cout<<"������"<<sjk[i].name<<'\t'<<"֤���ţ�"<<sjk[i].zjh<<endl;
            }
        }
    }
    return 0;
}

