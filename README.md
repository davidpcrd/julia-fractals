# Julia set generator (Fractal)
Generate julia set with Python
## Results
c = -0.75+0.11i
![image of a julia set with c = -0.75+0.11i](images/[-0.75+0.11i].10000x10000.png "c = -0.75+0.11i")

c = -0.443-0.592i
![image of a julia set with c = -0.443-0.592i](images/[-0.443+-0.592i].10000x10000.png "c = -0.443-0.592i")

c = -1.2+0i
![image of a julia set with c = -1.2+0i](images/[-1.2+0i].10000x10000.png "c = -1.2+0i")

c = 0.243+0.545i
![image of a julia set with c = 0.243+0.545i](images/[0.243+0.545i].10000x10000.png "c = 0.243+0.545i")

c = 0+0i
![image of a julia set with c = 0+0i](images/[0+0i].10000x10000.png "c = 0+0i")

## Set-up
```bash
pip install -r requirements.txt
python fractales.py
```

## Custom
To add custom c, go to ```fractales.py``` and in ```complexes``` add one
```python
complexes = [
    #                       a + bi
    Complex.from_algebra(0.243, 0.545),
    ### OR
    #      rho * cos(phi) + rho * sin(phi) * i
    Complex.from_trigo(rho, phi)
]
```

To change final dimension, change ```dim``` in ```fractales.py```

To change save path, change in ```fractales.py```
```python
img.save(f"images/[{c.a}+{c.b}i].{dim}x{dim}.png")
```