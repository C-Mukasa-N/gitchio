using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Pillar : MonoBehaviour
{
    public enum FireColor
    {
        Red,
        Orange,
        Green
    }

    public string pillarName;
    public List<Routine> routines;
    public FireColor color;
    
    public List<Routine> GetRoutines()
		{
		    return routines;
		}

		public void SetFireColor(FireColor newColor)
		{
		    color = newColor;
		    // code update l'apparence du feu du pilier.
		}
}