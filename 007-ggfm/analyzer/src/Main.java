import java.io.*;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        String returned_date, returned_days, real_date, real_days;
        boolean match;
        for (int ss=0; ss < 2000000000; ss+=86400){
            changeFile("num.txt", ss +"");

            String values[] = executer("./interface.sh").split("@");
            returned_date = values[0];
            returned_days = values[1];

            values = realValue(ss).split("@");
            real_date = values[0];
            real_days =values[1];
            match = returned_days.equals(real_days);
            if(match == false){
                System.out.println(returned_date + " # " + real_date + " # " + match);
            }
        }
    }

    public static String executer(String command){
        try {
            Runtime r = Runtime.getRuntime();
            Process p = r.exec(command);

            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(p.getInputStream()));

            return bufferedReader.readLine()+"@"+bufferedReader.readLine().substring(20);
        }catch (Exception e){
            System.out.println("Errore: " + e.getMessage());
            return "error";
        }
    }

    public static void changeFile(String path, String value){
        try {
            PrintWriter writer = new PrintWriter(path, "UTF-8");
            writer.println(value);
            writer.close();
        }catch (Exception e){
            System.out.println("Errore di scrittura file");
        }
    }

    public static String realValue(int seconds){
        LocalDateTime dateTime = LocalDateTime.ofEpochSecond(seconds, 0, ZoneOffset.UTC);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d-M-yyyy", Locale.ENGLISH);
        String formattedDate = dateTime.format(formatter);

        String giornomeseanno[] = formattedDate.split("-");
        int remainingDays = lastDayOfMonth(Integer.parseInt(giornomeseanno[1]),
                Integer.parseInt(giornomeseanno[2])) - Integer.parseInt(giornomeseanno[0]);

        return formattedDate+"@"+remainingDays; // Tuesday,November 1,2011 12:00,AM
    }

    public static int lastDayOfMonth (int month, int year)
    {
        Calendar cal = new GregorianCalendar(year, month-1, 1);
        cal.set(Calendar.DAY_OF_MONTH, cal.getActualMaximum (Calendar.DAY_OF_MONTH));
        return cal.getActualMaximum(Calendar.DAY_OF_MONTH);
    }
}
