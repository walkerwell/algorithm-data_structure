package language;


public class ClassLoadOrder {

    private ClassLoadOrder(){
        System.out.println("2 init add create");
    }

    /** 1 静态代码块 **/
    static {
        System.out.println("1 static block is create");
    }

    /** 2 静态变量 **/
    private static ClassLoadOrder addTwoNumbers = new ClassLoadOrder();

    /** 3 静态方法 **/
    public static void getMethod(){
        System.out.println("3 getMethod");
    }



    public static void main(String a[]){
        getMethod();
        System.out.println("main is end");
    }
}
