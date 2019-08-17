//公共Js
//模仿写一个 layer tips

function Common(){

};

Common.prototype.listenDownToggleClick = function(){
    //下拉菜单选项
    $(".down-box").hover(function(){
        console.log("hover running");
        $(this).find(".down-menu").animate({
            "opacity":1
        });
        $(this).find(".down-menu").show();
    },function(){
        $(this).find(".down-menu").animate({
            "opacity":0
        });
        $(this).find(".down-menu").hide();
    })
};

Common.prototype.run = function(){
    var self = this;
    self.listenDownToggleClick();
};

$(function(){
    var com = new Common();
    com.run();
});