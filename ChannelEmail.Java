package channel;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Base64;

public class ChannelEmail {

	static ChannelEmail api = new ChannelEmail();

	// Email
	public void PdfTextextractionService(String vChannel, String vImapServerName,
			String vImapPort, String vSubject, String vSender, String vComText) throws IOException {
		// JSON file
		final String POST_PARAMS = "{\n" + "\"Channel\":" + "\"" + vChannel + "\"" + ",\r\n"
				+ "    \"IMAPSERVERNAME\":" + "\"" + vImapServerName + "\",\r\n" + "    \"IMPAPSECUREPORT\":" + "\""
				+ vImapPort + "\",\r\n" + "    \"Subject_Doc_number\":" + "\"" + vSubject + "\",\r\n"
				+ "    \"Sendor\":" + "\"" + vSender + "\",\r\n" + "    \"Comparisontext\":" + "\"" + vComText
				+ "\"\n}";
		Connect(POST_PARAMS);
	}

	// Connection method
		public void Connect(String POST_PARAMS) throws IOException {
		System.out.println(POST_PARAMS);
 // Pass the service URL   
		URL obj = new URL("https://");
		HttpURLConnection postConnection = null;
		String userCredentials = "Username:Password";
		String basicAuth = "Basic " + new String(Base64.getEncoder().encode(userCredentials.getBytes()));

		try {
			postConnection = (HttpURLConnection) obj.openConnection();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		postConnection.setRequestProperty ("Authorization", basicAuth);
		postConnection.setRequestMethod("POST");
		postConnection.setRequestProperty("Content-Type", "application/json");
		postConnection.setDoOutput(true);
		OutputStream os = null;
		try {
			os = postConnection.getOutputStream();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		os.write(POST_PARAMS.getBytes());
		os.flush();
		os.close();
		int responseCode = postConnection.getResponseCode();
		if (responseCode == 200) {
			BufferedReader in = new BufferedReader(new InputStreamReader(postConnection.getInputStream()));
			String inputLine;
			StringBuffer response = new StringBuffer();
			while ((inputLine = in.readLine()) != null) {
				response.append(inputLine);
			}
			in.close();
			System.out.println(response.toString());
		} else {
			System.out.println("POST NOT WORKED");
		}
	}

	public static void main(String[] args) throws IOException {
		api.PdfTextextractionService("Email", "imap-mail.outlook.com", "993",
				"90007854", "", "Zahlungsbedingungen");

	}

}
