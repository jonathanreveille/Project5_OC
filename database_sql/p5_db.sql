-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema p5_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema p5_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `p5_db` DEFAULT CHARACTER SET utf8 ;
USE `p5_db` ;

-- -----------------------------------------------------
-- Table `p5_db`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`Category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `p5_db`.`Brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`Brand` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `brand_name` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `brand_name_UNIQUE` (`brand_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `p5_db`.`Favorite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`Favorite` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `idProduct` INT UNSIGNED NOT NULL,
  `substitute_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `p5_db`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`Product` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(45) NOT NULL,
  `nutriscore` VARCHAR(1) NOT NULL,
  `has_palm_oil` VARCHAR(3) NOT NULL,
  `about_product` TEXT NOT NULL,
  `url_name` VARCHAR(300) NOT NULL,
  `updated_time` DATETIME NOT NULL,
  `Category_id` INT UNSIGNED NOT NULL,
  `Brand_id` INT UNSIGNED NOT NULL,
  `Favorite_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `Category_id`, `Brand_id`, `Favorite_id`),
  UNIQUE INDEX `product_name_UNIQUE` (`product_name` ASC) VISIBLE,
  INDEX `fk_Product_Category1_idx` (`Category_id` ASC) VISIBLE,
  INDEX `fk_Product_Brand1_idx` (`Brand_id` ASC) VISIBLE,
  INDEX `fk_Product_Favorite1_idx` (`Favorite_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Category1`
    FOREIGN KEY (`Category_id`)
    REFERENCES `p5_db`.`Category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Brand1`
    FOREIGN KEY (`Brand_id`)
    REFERENCES `p5_db`.`Brand` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Favorite1`
    FOREIGN KEY (`Favorite_id`)
    REFERENCES `p5_db`.`Favorite` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `p5_db`.`Store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`Store` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `store_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `store_name_UNIQUE` (`store_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `p5_db`.`ProductStore`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `p5_db`.`ProductStore` (
  `Product_id` INT UNSIGNED NOT NULL,
  `Store_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_id`, `Store_id`),
  INDEX `fk_Product_has_Store_Store1_idx` (`Store_id` ASC) VISIBLE,
  INDEX `fk_Product_has_Store_Product_idx` (`Product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Store_Product`
    FOREIGN KEY (`Product_id`)
    REFERENCES `p5_db`.`Product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Store_Store1`
    FOREIGN KEY (`Store_id`)
    REFERENCES `p5_db`.`Store` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
