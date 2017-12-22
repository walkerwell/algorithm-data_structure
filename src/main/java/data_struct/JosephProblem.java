package data_struct;

public class JosephProblem {

    public static void main(String s[]){
        Person head = new Person(1);
        head.nextPerson = new Person(2,new Person(3,new Person(4, new Person(5,new Person(6,head)))));
        int m=1,n=6;
        while(n>1){
            if(m == 5 && head.isAlive) {
                System.out.println(head.num);
                head.isAlive = false;
                m=1;
                n--;
                while(!head.isAlive){
                    head=head.nextPerson;
                }
            }
            if(head.isAlive)
                m++;
            head = head.nextPerson;
        }
    }
}

class Person{
    public int num;
    public boolean isAlive = true;
    public Person nextPerson=null;

    public Person(int num) {
        this.num = num;
    }

    public Person(int num, Person nextPerson) {
        this.num = num;
        this.nextPerson = nextPerson;
    }
}
