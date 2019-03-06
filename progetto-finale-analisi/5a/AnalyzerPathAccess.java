import java.io.*;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;

public class AnalyzerPathAccess {
    public static String program_name;
    public static String filelog_name = "eacces.log"; //log path
    
    public static void main(String[] args) {
        String[] command = {"strace", "-ttfe", "trace=openat"};
        String[] command_and_args = concatenate(command, args);
        program_name = args[0];
        String result = terminalExecution(command_and_args);
        ArrayList<String> usefulLog = logIntegration(logFilter(result, "EACCES"));
        if(usefulLog.size() != 0){
            writeFile(filelog_name, usefulLog);
            System.out.println(filelog_name + " aggiornato con " + usefulLog.size() + " nuovo messaggio di log");
        }
        else
            System.out.println("Nessun accesso negato a file da parte di " + program_name);
    }

    /**
     * Esegue un comando terminale e ne ritorna l'output
     * @param command_and_args comando terminale da eseguire e relativi argomenti
     * @return output del comando eseguito sul terminale
     */
    public static String terminalExecution(String[] command_and_args){
        try {
            ProcessBuilder pb = new ProcessBuilder(command_and_args);
            pb.redirectErrorStream(true);
            Process p = pb.start();

            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(p.getInputStream()));

            String result = "";
            String s = "";
            do{
                    result += s + "\n";
                    s = bufferedReader.readLine();
            }while(s != null);

            return result;
        }catch (Exception e){
            System.out.println("Errore: " + e.getMessage());
            return "error";
        }
    }

    /**
     * Dati una serie di log (separati da '\n') ritorna solo i log contenenti la sottostringa specificata
     * @param logs log da filtrare
     * @param find sottostringa da cercare
     * @return log filtrati
     */
    public static ArrayList<String> logFilter(String logs, String find){
        String logsA[] = logs.split("\n");
        ArrayList<String> result = new ArrayList<>();
        for (String log : logsA) {
            if(log.contains(find))
                result.add(log);
        }
        return result;
    }

    /**
     * Integra i log con ulteriori informazioni relative all'acquisizione
     * @param logs lista di log da integrare
     * @return lista log con informazioni aggiuntive
     */
    public static ArrayList<String> logIntegration(ArrayList<String> logs){
        ArrayList<String> new_logs = new ArrayList<>();
        for (String log : logs){
            log = getTimestamp() + "\t" + program_name + "\t" + extractStringFromString(log) + "\t" + log;
            new_logs.add(log);
        }
        return new_logs;
    }

    /**
     * Estrae da una stringa la porzione delimitata dalle virgolette " "
     * es. openat(AT_FDCWD, "/var/run/acpid.pid", O_WRONLY|O.... ---> la funzione ritorna /var/run/acpid.pid
     * @param s stringa su cui effettuare l'operazione di estrazione
     * @return stringa che in s è delimitata da " "
     */
    public static String extractStringFromString(String s){
        try{
            return s.substring(s.indexOf("\"") + 1, s.lastIndexOf("\""));
        }catch(Exception e){
            return "";
        }
    }

    /**
     * Scrive dei valori in input su delle newline del file indicato, se non esiste lo crea
     * @param path file in cui scrivere
     * @param values valori da scrivere sul file
     */
    public static void writeFile(String path, ArrayList<String> values){
        try {
            PrintWriter writer = new PrintWriter(new FileOutputStream(new File(path), true /* append = true */));
            for (String s : values) {
                writer.printf(s + "\n");
            }
            writer.close();
        }catch (Exception e){
            System.out.println("Errore di scrittura file");
        }
    }

    /**
     * Ritorna la data del sistema
     * @return timestamp
     */
    public static String getTimestamp() {
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("YYYY-MM-dd HH:mm:ss");
        return sdf.format(cal.getTime());
    }


    /**
     * Concatena due array di stringhe
     * @param a primo array
     * @param b secondo array
     * @return array finale (primo array | secondo array)
     */
    public static String[] concatenate(String[] a, String[] b) {
        int aLen = a.length;
        int bLen = b.length;

        String[] c = new String[aLen + bLen];
        System.arraycopy(a, 0, c, 0, aLen);
        System.arraycopy(b, 0, c, aLen, bLen);
    
        return c;
    }
}