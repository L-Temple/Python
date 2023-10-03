local os = require("os");
local robot = require("robot")
local a=0
local invC = {}
local invetory = 1
local b=121  --总共向上放置格数,按照避雷针最高处减去最低处的Y坐标获得
local invS = {}
local invN = 1  --机器人初始选择的物品栏格子
while true do   --按照“几”字形移动并放置方块
    robot.select(invN)
    robot.turnAround()  --首先机器人会访问后侧的箱子获取方块，
    invS = robot.inventorySize() --获取机器人的物品栏格子数
    print("正在获取物品")
    for i=1,invS,1 do   --一次获取一组循环获取16次物品栏满
        robot.suck()  --从左边获取物品
    end
    robot.turnAround()
    print("正在向上放置方块")
    for d=a,b,1 do
        robot.detect()
        if true then   --判断前方有无方块，如果无则放置方块
            robot.place()  --放置方块，如果能放置则返回true，无法放置则返回false
            print ("正在放置第",d,"格方块")
            invC = robot.place()
            if invC == nil then  --如果第一个物品栏没有方块则返回nil
                robot.select(invetory+1)   --选择下一格物品栏
                invetory = invetory + 1
                robot.place()   --继续用新的格子放置方块
            robot.up()
            else         --前方没有方块则向上移动
                robot.up()
            end
        end
    end
    robot.turnRight()
    robot.forward()
    robot.turnLeft()
    robot.down()
    print("正在向下放置方块")
    for u=b,a,-1 do
        robot.detect()
        if true then   --判断前方有无方块，如果无则放置方块
            robot.place()  --放置方块，如果能放置则返回true，无法放置则返回false
            print ("正在放置第",u,"格方块")
            if invC == nil then  --如果第一个物品栏没有方块则返回nil

                robot.select(invetory+1)   --选择下一格物品栏
                invetory = invetory + 1
                robot.place()   --继续用新的格子放置方块
            robot.down()
            else         --前方没有方块则向下移动
                robot.down()
            end
        end
    end
    print("返回初始点")
    robot.turnLeft()
    robot.forward()
    robot.turnRight()
    print("休息30秒")
    os.sleep(30)   --设定机器人休息30秒，如果铁栅栏破坏比较快可以调低或者删除
end