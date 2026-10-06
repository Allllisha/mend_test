package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.text.StringSubstitutor;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Map;

/**
 * Mendスキャン練習用の小さなアプリ。
 * pom.xml の古いライブラリを実際に import して使うことで、
 * Reachability（脆弱なコードに到達するか）の分析対象になるようにしている。
 * 動かすことが目的ではなく、スキャンされることが目的。
 */
public class App {
    private static final Logger logger = LogManager.getLogger(App.class);

    public static void main(String[] args) throws Exception {
        String input = args.length > 0 ? args[0] : "{\"user\": \"arisa\"}";

        ObjectMapper mapper = new ObjectMapper();
        Map<?, ?> parsed = mapper.readValue(input, Map.class);
        logger.info("parsed input: {}", parsed);

        StringSubstitutor substitutor = StringSubstitutor.createInterpolator();
        String rendered = substitutor.replace("status: ${env:USER}");
        logger.info(rendered);
    }
}
