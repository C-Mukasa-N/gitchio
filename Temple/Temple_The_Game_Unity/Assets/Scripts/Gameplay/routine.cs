using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Routine : MonoBehaviour
{
    public enum RoutineColor
    {
        Red,
        Orange,
        Green
    }

    public string routineName;
    public List<Task> tasks;
    public RoutineColor color;
    
    public RoutineColor GetColor()
		{
		    return color;
		}
		
		public List<Task> GetTasks()
    {
        return tasks; // retourne la liste des tâches
    }

    public void SetColor(RoutineColor newColor)
    {
        color = newColor;
        // code pour update l'apparence de la routine
    }
}