<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>本机IP地址查询——By:Sugarguo</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
            <!-- 导航条 -->
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">
                            Toggle navigation
                        </span>
                        <span class="icon-bar">
                        </span>
                        <span class="icon-bar">
                        </span>
                        <span class="icon-bar">
                        </span>
                    </button>
                    <a class="navbar-brand" href="http://www.sugarguo.com/">
                        糖果果|Sugarguo
                    </a>
                </div>	
					
                    <ul class="nav navbar-nav navbar-right">
       <form class="navbar-form navbar-left" role="search" action="http://www.baidu.com/s?ie=UTF-8&wd=" target="_blank">
      <input type="text" class="form-control" id="name"  name="word"
         placeholder="请输入搜索项">
                        <button type="submit" class="btn btn-primary">
                            百度搜索
                        </button>		 
                    </form>
        </nav>
<p class="text-center"><span class="label label-info">你的IP是：</span></p>
        <h2><p class="text-center"><?php
$ip = $_SERVER["REMOTE_ADDR"];
echo '<p name="IP" class="text-center">', $ip, '</p>';
?></p></h2>
<?php
$start_time = microtime(true); //获取程序开始执行的时间
function getipCity($ip)
{
    $url = "http://ip.taobao.com/service/getIpInfo.php?ip=" . $ip;
    
    $ip = json_decode(file_get_contents($url));
    
    if ((string) $ip->code == '1') {
        return false;
        
    }
    
    $data = (array) $ip->data;
    
    return $data;
    
}
?>
<p class="text-center"><span class="label label-info">你的地址是：</span></p>
	<h3><p class="text-center"><?php
$b = getipCity($ip);
echo '<p name="Ad" class="text-center">', $b[country], ' ', $b[area], ' ', $b[region], ' ', $b[city], ' ', $b[county];
echo '<br/><p name="ISP" class="text-center">', $b[isp];
?> </p></p></p></h3>
<br/>
<h4><?php  ?></h4>
<h4><p class="text-center"><span class="label label-success"><?php
$end_time = microtime(true);
$total    = $end_time - $start_time;
$time = time();
echo '查询时间：',date("y-m-d h:i:s",$time),"<br/>	生成本页面执行了{$total}秒";
?></span></p></h4>


 <footer>
      <p class="text-center">&copy; 2015 <a href="http://www.sugarguo.com/" title="糖果果|Sugarguo">糖果果|Sugarguo</a>, Inc. All rights reserved.</p>
    </footer>


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
