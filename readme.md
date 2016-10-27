
## 为什么我会写blue_fariy.py

  `并不是所有人都愿意和他人分享自己所拥有的东西`<br/>
  
  很多时候,我们希望使用github 来托管自己的代码,但是又并不希望自己的代码共享出去,如果要真的这样做的话,需要创建github 私有项目,并不是每个人都愿意为此付费(其实我也没这个需求),所以能不能在git push 把代码推送到github 之前把我们写好的代码都加密呢?答案是肯定的..<br/>


## 如何使用blue_fariy.py

  示例项目地址:https://github.com/lcatro/blue_fariy_demo<br/>

  首先,我们创建一个空项目<br/>

![create_repo](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/create_repo.png)<br/>

  项目里面有一个文件,*readme.md* <br/>

![demo_example](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/demo_example.png)<br/>

  接下来做第一次commit ,这次commit 里我们只上传python 文件<br/>

![first_commit_command](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/first_commit_command.png)<br/>

  上传结束之后,github 项目里只有这个python 文件<br/>

![first_commit_success](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/first_commit_success.png)<br/>

  然后使用`blue_fariy.py` ,过程很简单,第一步输入命令:`.\\blue_fariy.py push` 生成bat 文件,第二步输入命令:`.\\push.bat` 进行推送<br/>
  
![push_to_github](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/push_to_github.png)<br/>

  同时,在目录下面创建了三个新文件,一个是由`blue_fariy.py` 生成的bat 文件,它负责对工程进行加密和推送部分;另一个文件是RSA 的密钥文件,用于解开`packet.pck` ,最后我们就是把这个加密过后的文件上传到github <br/>

![new_files](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/new_files.png)<br/>

  上传到github 之后,只剩下python 文件和被加密的项目文件<br/>
  
![using_blue_fariy_push](https://raw.githubusercontent.com/lcatro/blue_fariy/master/demo_picture/using_blue_fariy_push.png)<br/>

