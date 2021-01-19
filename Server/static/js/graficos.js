var gauge1 = loadLiquidFillGauge("fillgauge1", 55);
var config1 = liquidFillGaugeDefaultSettings();
config1.circleColor = "#FF7777";
config1.textColor = "#FF4444";
config1.waveTextColor = "#FFAAAA";
config1.waveColor = "#FFDDDD";
config1.circleThickness = 0.2;
config1.textVertPosition = 0.2;
config1.waveAnimateTime = 1000;
var gauge2= loadLiquidFillGauge("fillgauge2", 28, config1);
var config2 = liquidFillGaugeDefaultSettings();
config2.circleColor = "#D4AB6A";
config2.textColor = "#553300";
config2.waveTextColor = "#805615";
config2.waveColor = "#AA7D39";
config2.circleThickness = 0.1;
config2.circleFillGap = 0.2;
config2.textVertPosition = 0.8;
config2.waveAnimateTime = 2000;
config2.waveHeight = 0.3;
config2.waveCount = 1;
var gauge3 = loadLiquidFillGauge("fillgauge3", 60.1, config2);
var config3 = liquidFillGaugeDefaultSettings();
config3.textVertPosition = 0.8;
config3.waveAnimateTime = 5000;
config3.waveHeight = 0.15;
config3.waveAnimate = false;
config3.waveOffset = 0.25;
config3.valueCountUp = false;
config3.displayPercent = false;

function NewValue(){
    if(Math.random() > .5){
        return Math.round(Math.random()*100);
    } else {
        return (Math.random()*100).toFixed(1);
    }
}