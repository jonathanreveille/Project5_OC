-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema p5_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema p5_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `p5_db` DEFAULT CHARACTER SET utf8 ;
USE `p5_db` ;

-- -----------------------------------------------------
-- Table `p5_db`.`brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`brand` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `brand_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `brand_brand_name` (`brand_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 244
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `p5_db`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`category` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `category_category_name` (`category_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `p5_db`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`product` (
  `code` BIGINT(20) NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `url` VARCHAR(255) NOT NULL,
  `nutrition_grade_fr` VARCHAR(1) NOT NULL,
  `brand_id` INT(11) NOT NULL,
  `category_id` INT(11) NOT NULL,
  PRIMARY KEY (`code`),
  INDEX `product_brand_id` (`brand_id` ASC) VISIBLE,
  INDEX `product_category_id` (`category_id` ASC) VISIBLE,
  CONSTRAINT `product_ibfk_1`
    FOREIGN KEY (`brand_id`)
    REFERENCES `p5_db`.`brand` (`id`),
  CONSTRAINT `product_ibfk_2`
    FOREIGN KEY (`category_id`)
    REFERENCES `p5_db`.`category` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `p5_db`.`favorite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`favorite` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `substituted_product_id` BIGINT(20) NOT NULL,
  `substitute_products_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `favorite_substituted_product_id` (`substituted_product_id` ASC) VISIBLE,
  INDEX `favorite_substitute_products_id` (`substitute_products_id` ASC) VISIBLE,
  CONSTRAINT `favorite_ibfk_1`
    FOREIGN KEY (`substituted_product_id`)
    REFERENCES `p5_db`.`product` (`code`),
  CONSTRAINT `favorite_ibfk_2`
    FOREIGN KEY (`substitute_products_id`)
    REFERENCES `p5_db`.`product` (`code`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `p5_db`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`store` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `store_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `store_store_name` (`store_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 90
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `p5_db`.`product_store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`product_store` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `product_id` BIGINT(20) NOT NULL,
  `store_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `productstore_product_id_store_id` (`product_id` ASC, `store_id` ASC) VISIBLE,
  INDEX `productstore_product_id` (`product_id` ASC) VISIBLE,
  INDEX `productstore_store_id` (`store_id` ASC) VISIBLE,
  CONSTRAINT `product_store_ibfk_1`
    FOREIGN KEY (`product_id`)
    REFERENCES `p5_db`.`product` (`code`),
  CONSTRAINT `product_store_ibfk_2`
    FOREIGN KEY (`store_id`)
    REFERENCES `p5_db`.`store` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1655
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
