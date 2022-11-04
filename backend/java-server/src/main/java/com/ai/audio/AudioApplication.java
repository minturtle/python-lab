package com.ai.audio;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.concurrent.TimeUnit;

@SpringBootApplication
public class AudioApplication {

	public static final String UPLOAD_FILE_PATH = "C:\\Users\\minseok kim\\PycharmProjects\\lab1\\backend\\sample\\";
	public static final String PYTHON_MODULE_PATH = "C:\\Users\\minseok kim\\PycharmProjects\\lab1\\backend\\java-server\\python-module";
	public static void main(String[] args) {
		SpringApplication.run(AudioApplication.class, args);
	}

	@Bean
	public CommandLineRunner start(){
		return (args)->{
			final File pythonFolder = new File(PYTHON_MODULE_PATH);
			Process p = Runtime.getRuntime().exec("python audio_converter.py " +UPLOAD_FILE_PATH + "audio-ko.mp3", null,pythonFolder);
			if(!p.waitFor(5, TimeUnit.MINUTES)){
				p.destroy();
			}

			BufferedReader stdIn = new BufferedReader(new InputStreamReader(p.getInputStream()));
			final BufferedReader stdErr = new BufferedReader(new InputStreamReader(p.getErrorStream()));

			String s = null;
			while ((s = stdIn.readLine()) != null) System.out.println(s);

			while ((s = stdErr.readLine()) != null) System.out.println(s);

			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			System.out.println(p.waitFor());
		};

	}

}
