
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


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
