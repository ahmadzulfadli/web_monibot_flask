CREATE DATABASE iot_monibot;

use iot_monibot;

CREATE TABLE `monibot` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_temp` float NOT NULL,
  `data_humd` float NOT NULL,
  `data_ppmch4` float NOT NULL,
  `data_ppmco` float NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
SELECT *FROM monibot;

DESC monibot;

