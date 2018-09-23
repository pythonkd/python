# 1.模块
- 如何定义模块
    - 函数功能单一
    - 类（相似功能的组合，或者类似业务模块）高内聚低耦合
    - 测试代码
- 如何使用模块
    - 模块直接导入
        - 假入模块名称直接以数字开头，需要借助importlib里的import_module 
    - 语法
    
        import module_name
        module_.function_name
        module_name.class_name
    
    - import 模块as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
        
    - from module_name import func_name ,class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，**不需要前缀**
    - from module_name import *
        -导入模块所有内容
        
- 'if __name__=="__main__"' 的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都已此代码为入口
    
# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径：
    -加载模块的时候，系统会在哪些地方搜寻此模块
- 系统默认的模块搜索路径

    import sys
    sys.path 属性可以获取搜索路径列表
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    1.搜索内存中已经加载好的模块
    2.搜索Python的内置模块
    3.搜索sys.path路径
    
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包结构

-包的导入操作
    - import package_name
        -直接导入一个包，可以使用__init__.py中的内容
        -使用方式：
            
            package_name.func_name
            package_name.class_name.func_name()
        - 此种方式的访问内容是
        - import package_name as p
            -具体用法跟上面简单导入一致
            -主义的此种方法默认对__init__.py内容的导入
            
    - import package.module
        -导入包中某一个具体的模块
        -使用方法
        
            package.module.func_name
            package.module.class.fun()
            package.module.class.var
        import package.module as pm
-from ...import导入
    -from package import module1,module02
    -此种导入方法不执行__init__的内容

        from pkg01.import p01
        p01.sayHello()
    - from package import *
        -导入当前包'__init__.py'文件中所有的函数和类
    -使用方法
        func_name()
        class_name.func_name()
        class_name.var
-from package.module import *
    -导入包中指定的模块的所有内容
    -使用方法
        - func_name()
          class_name.func_name()
-在开发环境中经常会用其他模块，可以在当前包中直接导入其他模块中的内容
    -import完整的包或者模块的路径
- ‘__all__'的用法
    -在使用from package import*的时候，* 可以导入的内容
    -'__init__.py'中如果文件为空，或者没有‘__all__'那么这可以把’__init__'中的导入
    - ‘__init__'如果设置了’__all__'的值，那么则按照‘__all__'指定的子包或者模块
    进行,则不会载入’__init__'中的内容
    -‘__all__=['module','module2','package1'......]'
