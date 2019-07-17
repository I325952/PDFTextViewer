package channel;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class FileLocation {

	public static void main(String args[]) throws IOException {

		// Connect to the web server endpoint - Pass the service URL
		URL serverUrl = new URL("");
		HttpURLConnection urlConnection = (HttpURLConnection) serverUrl.openConnection();

		String boundaryString = "----WebKitFormBoundary7MA4YWxkTrZu0gW";
    // Pass the PDF file local location
		String fileUrl = "";
		File logFileToUpload = new File(fileUrl);

		// Indicate that we want to write to the HTTP request body
		urlConnection.setDoOutput(true);
		urlConnection.setRequestMethod("POST");
		urlConnection.addRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundaryString);

		OutputStream outputStreamToRequestBody = urlConnection.getOutputStream();

		BufferedWriter httpRequestBodyWriter = new BufferedWriter(new OutputStreamWriter(outputStreamToRequestBody));

		// Include value from the myFileDescription text area in the post data
		httpRequestBodyWriter.write("\n\n--" + boundaryString + "\n");
		httpRequestBodyWriter.write("Content-Disposition: form-data; name=\"file\"");
		httpRequestBodyWriter.write("\n\n");

		// Include the section to describe the file
		httpRequestBodyWriter.write("\n--" + boundaryString + "\n");
		httpRequestBodyWriter.write("Content-Disposition: form-data;" + "name=\"file\";" + "filename=\""
				+ logFileToUpload.getName() + "\"" + "\nContent-Type: application/pdf\n\n");

		httpRequestBodyWriter.flush();

		// Write the actual file contents
		@SuppressWarnings("resource")
		FileInputStream inputStreamToLogFile = new FileInputStream(logFileToUpload);

		int bytesRead;
		byte[] dataBuffer = new byte[1024];

		while ((bytesRead = inputStreamToLogFile.read(dataBuffer)) != -1) {

			outputStreamToRequestBody.write(dataBuffer, 0, bytesRead);
		}

		outputStreamToRequestBody.flush();

		// Mark the end of the multipart http request
		httpRequestBodyWriter.write("\n--" + boundaryString + "--\n");
		httpRequestBodyWriter.flush();

		// Close the streams
		outputStreamToRequestBody.close();
		httpRequestBodyWriter.close();

		BufferedReader httpResponseReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
		String lineRead;
		while ((lineRead = httpResponseReader.readLine()) != null) {
			System.out.println(lineRead);
		}

	}
}
