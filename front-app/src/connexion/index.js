import React, { Component } from 'react'
import './index.css'
import {useHistory} from 'react-router-dom'

export default function Connexion() {
    return (
        <div>
            <div className="form">
                <form>
                <h1>Connexion</h1>
                    <div>
                        <label htmlFor="">email</label>
                        <input class="anim" type="email" />
                    </div>
                    <div>
                        <label htmlFor="">Mot de passe</label>
                        <input class="anim" type="password" />
                    </div>
                    <button onClick="trans">Log In</button>
                </form>
            </div>
        </div>
    )
}