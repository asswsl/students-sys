/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 80100
 Source Host           : localhost:3306
 Source Schema         : students-sys

 Target Server Type    : MySQL
 Target Server Version : 80100
 File Encoding         : 65001

 Date: 30/09/2023 16:17:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `english` int NOT NULL,
  `python` int NOT NULL,
  `java` int NOT NULL,
  `grade` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (1001, 'wq', 99, 88, 88, 275);
INSERT INTO `students` VALUES (1002, 'wr', 99, 99, 99, 297);
INSERT INTO `students` VALUES (1003, 'ww', 77, 77, 77, 231);

SET FOREIGN_KEY_CHECKS = 1;
