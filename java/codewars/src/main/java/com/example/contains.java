package com.example;

public class contains {
    public static boolean solution(String str, String ending) {
    return str.endsWith(ending);
}

public static String maskify(String str) {
        if (str == null) return null;
        if (str.length() <= 4) return str;
        String visiblePart = str.substring(str.length() - 4);
        StringBuilder maskedPart = new StringBuilder();
        for (int i = 0; i < str.length() - 4; i++) {
            maskedPart.append("#");
        }
        return maskedPart.toString() + visiblePart;
    }

    public static int duplicateCount(String text) {
        if (text == null) return 0;
        text = text.toLowerCase();
        int count = 0;
        for (char c = 'a'; c <= 'z'; c++) {
            int first = text.indexOf(c);
            if (first != -1 && first == text.lastIndexOf(c)) {
                count++;
            }
        }
        return count;
    }

    public static boolean getXO (String str) {
        return str == null || str.toLowerCase().replace("o", "").length() == str.toLowerCase().replace("x", "").length();
    }
}