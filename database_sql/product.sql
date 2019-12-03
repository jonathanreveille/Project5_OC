
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
