var isAnimated = false;
$(document).ready(function(){
    $(window).on("scroll",function(){
        //this代表window scrollTop()向上滑动的距离
        if($(this).scrollTop() > 450){
            $(".left-side").addClass("colorChan");
            $(".gotop").addClass("tops");
            if(!isAnimated){
                $(".left-side").css("margin","0");
                $(".left-side").animate({"margin":"0"},1000);
                isAnimated = true;
            }
        }else{
            isAnimated = false;
            $(".left-side").removeClass("colorChan");
            $(".gotop").removeClass("tops");
        }
    })
});
// 回顶端二道按钮
var goto_top_type = -1;
var goto_top_itv = 0;

function goto_top_timer() {
    var y = goto_top_type == 1 ? document.documentElement.scrollTop
            : document.body.scrollTop;
    var moveby = 40;
    y -= Math.ceil(y * moveby / 100);
    if (y < 0) {
        y = 0;
    }
    if (goto_top_type == 1) {
        document.documentElement.scrollTop = y;
    } else {
        document.body.scrollTop = y;
    }
    if (y == 0) {
        clearInterval(goto_top_itv);
        goto_top_itv = 0;
    }
}

function goto_top() {
    if (goto_top_itv == 0) {
        if (document.documentElement && document.documentElement.scrollTop) {
            goto_top_type = 1;
        } else if (document.body && document.body.scrollTop) {
            goto_top_type = 2;
        } else {
            goto_top_type = 0;
        }
        if (goto_top_type > 0) {
            goto_top_itv = setInterval('goto_top_timer()', 50);
        }
    }
}

// 侧边菜单栏
$(function(){
  var menuwidth  = 340; // 边栏宽度
  var menuspeed  = 400; // 边栏滑出耗费时间

  var $bdy       = $('body');
  var $container = $('.main');
  var $burger    = $('#hamburgermenu');
  var negwidth   = "-"+menuwidth+"px";
  var poswidth   = menuwidth+"px";

  $('.left-side').on('click',function(e){
    if($bdy.hasClass('openmenu')) {
      jsAnimateMenu('close');
    } else {
      jsAnimateMenu('open');
    }
  });

  $('.overlay').on('click', function(e){
    if($bdy.hasClass('openmenu')) {
      jsAnimateMenu('close');
    }
  });
  function jsAnimateMenu(tog) {
    if(tog == 'open') {
      $bdy.addClass('openmenu');
      $container.animate({marginRight: negwidth, marginLeft: poswidth}, menuspeed);
      $burger.animate({width: poswidth}, menuspeed);
      $('.overlay').animate({left: poswidth}, menuspeed);
    }

    if(tog == 'close') {
      $bdy.removeClass('openmenu');

      $container.animate({marginRight: "0", marginLeft: "0"}, menuspeed);
      $burger.animate({width: "0"}, menuspeed);
      $('.overlay').animate({left: "0"}, menuspeed);
    }
  }
});

// 左边滚轮样式
 $(".side-box").niceScroll({
    cursorcolor: "#f75357",   //滚动条颜色
    cursoropacitymax: 0.5, //滚动条透明度
    cursorwidth:"3px",
    cursorborder:"0",
    cursorborderradius:"5px"


 });
  $("body").niceScroll({
        cursorcolor: "aquamarine",   //滚动条颜色
        cursoropacitymax: 1, //滚动条透明度
        gesturezoom: true,
        spacebarenabled: true, // 当按下空格时使页面向下滚动
        preventmultitouchscrolling: true,  // 防止多触点时间引发滚动
        cursorwidth:"8px",
        cursorborder:"0",
        cursorborderradius:"3px",
      enablescrollonselection: true, // 当选择文本时激活内容自动滚动

  });

  // 改变拖动条后重新定义鼠标样式

  $(document).ready(function(){
				$("div").mouseover(function(filename){
					//$("input.btn").hide();
					$(this).css("cursor","auto");
				});
  });

  // ajax提交
function AjaxSubmit(type) {
    var input_dict={};
    $("input").each(function () {
        var v = $(this).val();   //获取循环当前input标签的内容
        var cons = $("textarea").val();
        var n = $(this).attr("name");  //获取X循环当前input 的标签
        var n1 = $("textarea").attr("name");
        input_dict[n] = v;       //生成字典:{'属性值':'标签输入的内容'},{'con':deocde}
        input_dict[n1]=cons;
        input_dict['type'] = type;
    });
    $.ajax({
            url:'/tools/base64s/',
            type:'POST',
            dataType:"JSON",
            data:input_dict,
            success:function (data) {
                $("textarea").text(data.msg);
            },
            error:function () {
                alert("错误!请检查内容输入!");
            }
        })
}

function AjaxSubmitH(type) {
    var input_dict={};
    $("input").each(function () {
        var v = $(this).val();   //获取循环当前input标签的内容
        var cons = $("textarea").val();
        var n = $(this).attr("name");  //获取X循环当前input 的标签
        var n1 = $("textarea").attr("name");
        input_dict[n] = v;       //生成字典:{'属性值':'标签输入的内容'},{'con':deocde}
        input_dict[n1]=cons;
        input_dict['type'] = type;
        console.log(input_dict)
    });
    $.ajax({
            url:'/tools/htmls/',
            type:'POST',
            dataType:"JSON",
            data:input_dict,
            success:function (data) {
                $("textarea").text(data.msg);
            },
            error:function () {
                alert("请检查内容输入！");
            }
        })
}