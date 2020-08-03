<template>
    <div class="add-smoothie container">
        <h2 class="center-align indigo-text">Add New Smoothie Recipe</h2>
        <form @submit.prevent="addSmoothie">
            <div class="field title">
                <label for="title">Smoothie Title:</label>
                <input type="text" name="title" v-model="title">
            </div>
            <div v-for="(ingredient, index) of ingredients" :key="index" class="field">
                <label for="ingredient">Ingredient:</label>
                <input type="text" name="ingredient" v-model="ingredients[index]">
                <i class="material-icons delete" @click="deleteIngredient(ingredient)">delete</i>

            </div>
            <div v-if="title" class="field add-ingredient">
                <label for="add-ingredient">Ad an ingredient:</label>
                <input type="text" name="add-ingredient" @keydown.tab.prevent="addIngredient" v-model="ingredient">
                <i class="material-icons delete" @click="deleteIngredient(ingredient)">delete</i>
            </div>
            <div class="field center-align">
                <p v-if="feedback" class="red-text">{{ feedback }}</p>
                <button class="btn pink">Add Smoothie</button>
                <button class="btn pink" @click="reset">Reset</button>
            </div>
        </form>
    </div>
</template>

<script>
import db from '@/firebase/init'
import slugify from 'slugify'

export default {
    name: 'AddSmoothie',
    data() {
        return {
            title: null,
            ingredient: null,
            ingredients: [],
            feedback: null,
            slug: null
        }
    },
    methods: {
        addSmoothie() {
            if(this.title){
                this.feedback = null
                this.slug = slugify(this.title, {
                    replacement: '-',
                    remove: /[$*_+~.()'"!\-:@]/g,
                    lower: true
                })
                fetch('http://localhost:5000/api/v1/smoothies/new', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: this.title,
                        ingredients: this.ingredients
                    })
                }).then(() => {
                    this.$router.push({ name: 'Index' })
                }).catch(err => console.log(err))
            }else {
                this.feedback = "You must enter a smoothie title"
            }
        },
        addIngredient() {
            if(this.ingredient){
                this.ingredients.push(this.ingredient)
                this.ingredient = null
                this.feedback = null
            }
            else{
                this.feedback = "You must enter a value in order to add an ingredient"
            }
        },
        deleteIngredient(ingredientToRemove) {
            this.ingredients = this.ingredients.filter(ingredient => ingredient !== ingredientToRemove)
        },
        reset(){
            this.title = null
            this.ingredients = null
        }
    }
}
</script>

<style>
    .add-smoothie{
        margin-top: 60px;
        padding: 20px;
        max-width: 500px;
    }
    .add-smoothie h2{
        font-size: 2em;
        margin: 20px auto;
    }
    .add-smoothie .field{
        margin: 20px auto;
        position: relative;
    }
    .add-smoothie .delete{
        cursor: pointer; 
        position: absolute;
        right: 0;
        bottom: 16px;
        color: #aaa;
        font-size: 1.4em;
    }
</style>