<div class="container">

        <div class="row">

            <!-- Blog Post Content Column -->
            <div class="col-lg-8">
                <form action="<?php echo $_SERVER["PHP_SELF"]?>" method="post">
                   <!-- Blog Post -->

                    <!-- Title -->
                    <p>
                    <label></label><input type="text" name="title" />
                    </p>
                    <!-- Author -->
                    <p class="lead">
                        by <a href="#">Anonymous</a>
                    </p>
                    <p> 
                    <label for="body">Body:</label>
                    </p>
                    <textarea name="body" cols=50 rows=10></textarea>
                    <p>
                    <label> Category:</label>
                    <select name="category">
                        <?php
                            $query = $db->query("SELECT * FROM categories");
                            while($row = $query->fetch_object()) {
                                echo "<option value='".$row->category_id."'>".$row->category."</option>";
                            }
                        ?>
                    </select>
                    </p>
                    <input type="submit" name="submit" value="Submit" />
                    <hr>
                    <hr>
                        
                </form> 

           
            </div>