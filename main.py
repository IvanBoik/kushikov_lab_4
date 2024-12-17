from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from scipy. integrate import odeint
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="static/templates")

def du4_dt(u,t,c):

        [p0_t, p1_t, p2_t, p3_t, p4_t, p5_t, p6_t, p7_t, p8_t, p9_t, p10_t, p11_t, p12_t, p13_t, p14_t, p15_t,
         p16_t, p17_t, p18_t, p19_t, p20_t, p21_t, p22_t, p23_t, p24_t, p25_t, p26_t, p27_t, p28_t, p29_t, p30_t, p31_t] = u

        dp0_dt = (
            - p0_t * (c['l1'] + c['l2'] + c['l3'] + c['l4'] + c['l5'])
            + c['u1'] * p1_t
            + c['u2'] * p2_t
            + c['u3'] * p3_t
            + c['u4'] * p4_t
            + c['u5'] * p5_t
        ) 

        dp1_dt = (
            - p1_t * (c['u1'] + c['l2'] + c['l3'] + c['l4'] + c['l5'])
            + c['l1'] * p0_t
            + c['u2'] * p6_t
            + c['u3'] * p7_t
            + c['u4'] * p9_t
            + c['u5'] * p10_t
        ) 

        dp2_dt = (
            - p2_t * (c['u2'] + c['l1'] + c['l3'] + c['l4'] + c['l5'])
            + c['l2'] * p0_t
            + c['u1'] * p8_t
            + c['u3'] * p6_t
            + c['u4'] * p11_t
            + c['u5'] * p12_t
        ) 

        dp3_dt = (
            - p3_t * (c['u3'] + c['l1'] + c['l2'] + c['l4'] + c['l5'])
            + c['l3'] * p0_t
            + c['u1'] * p7_t
            + c['u2'] * p8_t
            + c['u4'] * p13_t
            + c['u5'] * p14_t
        ) 

        dp4_dt = (
            - p4_t * (c['u4'] + c['l1'] + c['l2'] + c['l3'] + c['l5'])
            + c['l3'] * p0_t
            + c['u1'] * p9_t
            + c['u2'] * p11_t
            + c['u3'] * p13_t
            + c['u5'] * p15_t
        ) 

        dp5_dt = (
            - p5_t * (c['l4'] + c['l1'] + c['l2'] + c['l3'] + c['u5'])
            + c['l5'] * p0_t
            + c['u1'] * p10_t
            + c['u2'] * p12_t
            + c['u3'] * p14_t
            + c['u4'] * p15_t
        )

        dp6_dt = (
            - p6_t * (c['u1'] + c['u2'] + c['l3'] + c['l4'] + c['l5'])
            + c['l1'] * p2_t
            + c['l2'] * p1_t
            + c['u3'] * p16_t
            + c['u4'] * p17_t
            + c['u5'] * p18_t
        ) 

        dp7_dt = (
            - p7_t * (c['u1'] + c['l2'] + c['u3'] + c['l4'] + c['l5'])
            + c['l1'] * p3_t
            + c['u2'] * p16_t
            + c['l3'] * p1_t
            + c['u4'] * p19_t
            + c['u5'] * p20_t
        ) 

        dp8_dt = (
            - p8_t * (c['l1'] + c['u2'] + c['u3'] + c['l4'] + c['l5'])
            + c['u1'] * p16_t
            + c['l2'] * p3_t
            + c['l3'] * p2_t
            + c['u4'] * p21_t
            + c['u5'] * p22_t
        ) 

        dp9_dt = (
            - p9_t * (c['u1'] + c['l2'] + c['l3'] + c['u4'] + c['l5'])
            + c['l1'] * p4_t
            + c['u2'] * p17_t
            + c['u3'] * p19_t
            + c['l4'] * p1_t
            + c['u5'] * p23_t
        ) 

        dp10_dt = (
            - p10_t * (c['u1'] + c['l2'] + c['l3'] + c['l4'] + c['u5'])
            + c['l1'] * p5_t
            + c['u2'] * p18_t
            + c['u3'] * p20_t
            + c['u4'] * p23_t
            + c['l5'] * p1_t
        ) 

        dp11_dt = (
            - p11_t * (c['l1'] + c['u2'] + c['l3'] + c['u4'] + c['l5'])
            + c['u1'] * p17_t
            + c['l2'] * p4_t
            + c['u3'] * p21_t
            + c['l4'] * p2_t
            + c['u5'] * p24_t
        ) 

        dp12_dt = (
            - p12_t * (c['l1'] + c['u2'] + c['l3'] + c['l4'] + c['u5'])
            + c['u1'] * p18_t
            + c['l2'] * p5_t
            + c['u3'] * p22_t
            + c['u4'] * p24_t
            + c['l5'] * p2_t
        ) 

        dp13_dt = (
            - p13_t * (c['l1'] + c['l2'] + c['u3'] + c['u4'] + c['l5'])
            + c['u1'] * p19_t
            + c['u2'] * p21_t
            + c['l3'] * p4_t
            + c['l4'] * p3_t
            + c['u5'] * p25_t
        ) 

        dp14_dt = (
            - p14_t * (c['l1'] + c['l2'] + c['u3'] + c['l4'] + c['u5'])
            + c['u1'] * p20_t
            + c['u2'] * p22_t
            + c['l3'] * p5_t
            + c['u4'] * p25_t
            + c['l5'] * p3_t
        ) 

        dp15_dt = (
            - p15_t * (c['l1'] + c['l2'] + c['l3'] + c['u4'] + c['u5'])
            + c['u1'] * p23_t
            + c['u2'] * p24_t
            + c['u3'] * p25_t
            + c['l4'] * p5_t
            + c['l5'] * p4_t
        ) 

        dp16_dt = (
            - p16_t * (c['u1'] + c['u2'] + c['u3'] + c['l4'] + c['l5'])
            + c['l1'] * p8_t
            + c['l2'] * p7_t
            + c['l3'] * p6_t
            + c['u4'] * p26_t
            + c['u5'] * p27_t
        ) 

        dp17_dt = (
            - p17_t * (c['u1'] + c['u2'] + c['l3'] + c['u4'] + c['l5'])
            + c['l1'] * p11_t
            + c['l2'] * p9_t
            + c['u3'] * p26_t
            + c['l4'] * p6_t
            + c['u5'] * p28_t
        ) 

        dp18_dt = (
            - p18_t * (c['u1'] + c['u2'] + c['l3'] + c['l4'] + c['u5'])
            + c['l1'] * p12_t
            + c['l2'] * p10_t
            + c['u3'] * p27_t
            + c['u4'] * p28_t
            + c['l5'] * p6_t
        ) 

        dp19_dt = (
            - p19_t * (c['u1'] + c['l2'] + c['u3'] + c['u4'] + c['l5'])
            + c['l1'] * p13_t
            + c['u2'] * p26_t
            + c['l3'] * p9_t
            + c['l4'] * p7_t
            + c['u5'] * p29_t
        ) 

        dp20_dt = (
            - p20_t * (c['u1'] + c['l2'] + c['u3'] + c['l4'] + c['u5'])
            + c['l1'] * p14_t
            + c['u2'] * p27_t
            + c['l3'] * p10_t
            + c['u4'] * p29_t
            + c['l5'] * p7_t
        ) 

        dp21_dt = (
            - p21_t * (c['l1'] + c['u2'] + c['u3'] + c['u4'] + c['l5'])
            + c['u1'] * p26_t
            + c['l2'] * p13_t
            + c['l3'] * p11_t
            + c['l4'] * p8_t
            + c['u5'] * p30_t
        ) 

        dp22_dt = (
            - p22_t * (c['l1'] + c['u2'] + c['u3'] + c['l4'] + c['u5'])
            + c['u1'] * p27_t
            + c['l2'] * p14_t
            + c['l3'] * p12_t
            + c['u4'] * p30_t
            + c['l5'] * p8_t
        ) 

        dp23_dt = (
            - p23_t * (c['u1'] + c['l2'] + c['l3'] + c['u4'] + c['u5'])
            + c['l1'] * p15_t
            + c['u2'] * p28_t
            + c['u3'] * p29_t
            + c['l4'] * p10_t
            + c['l5'] * p9_t
        ) 

        dp24_dt = (
            - p24_t * (c['l1'] + c['u2'] + c['l3'] + c['u4'] + c['u5'])
            + c['u1'] * p28_t
            + c['l2'] * p15_t
            + c['u3'] * p30_t
            + c['l4'] * p12_t
            + c['l5'] * p11_t
        ) 

        dp25_dt = (
            - p25_t * (c['l1'] + c['l2'] + c['u3'] + c['u4'] + c['u5'])
            + c['u1'] * p29_t
            + c['u2'] * p30_t
            + c['l3'] * p15_t
            + c['l4'] * p14_t
            + c['l5'] * p13_t
        ) 

        dp26_dt = (
            - p26_t * (c['u1'] + c['u2'] + c['u3'] + c['u4'] + c['l5'])
            + c['l1'] * p21_t
            + c['l2'] * p19_t
            + c['l3'] * p17_t
            + c['l4'] * p16_t
            + c['u5'] * p31_t
        ) 

        dp27_dt = (
            - p27_t * (c['u1'] + c['u2'] + c['u3'] + c['l4'] + c['u5'])
            + c['l1'] * p22_t
            + c['l2'] * p20_t
            + c['l3'] * p18_t
            + c['u4'] * p31_t
            + c['l5'] * p16_t
        ) 

        dp28_dt = (
            - p28_t * (c['u1'] + c['u2'] + c['l3'] + c['u4'] + c['u5'])
            + c['l1'] * p24_t
            + c['l2'] * p23_t
            + c['u3'] * p31_t
            + c['l4'] * p18_t
            + c['l5'] * p17_t
        ) 

        dp29_dt = (
            - p29_t * (c['u1'] + c['l2'] + c['u3'] + c['u4'] + c['u5'])
            + c['l1'] * p25_t
            + c['u2'] * p31_t
            + c['l3'] * p23_t
            + c['l4'] * p20_t
            + c['l5'] * p19_t
        ) 

        dp30_dt = (
            - p30_t * (c['l1'] + c['u2'] + c['u3'] + c['u4'] + c['u5'])
            + c['u1'] * p31_t
            + c['l2'] * p25_t
            + c['l3'] * p24_t
            + c['l4'] * p22_t
            + c['l5'] * p21_t
        ) 

        dp31_dt = (
            - p31_t * (c['u1'] + c['u2'] + c['u3'] + c['u4'] + c['u5'])
            + c['l1'] * p30_t
            + c['l2'] * p29_t
            + c['l3'] * p28_t
            + c['l4'] * p27_t
            + c['l5'] * p26_t
        ) 

        return [dp0_dt, dp1_dt, dp2_dt, dp3_dt, dp4_dt, dp5_dt, dp6_dt, dp7_dt, dp8_dt, dp9_dt, dp10_dt, dp11_dt, dp12_dt, dp13_dt, dp14_dt, dp15_dt,
                dp16_dt, dp17_dt, dp18_dt, dp19_dt, dp20_dt, dp21_dt, dp22_dt, dp23_dt, dp24_dt, dp25_dt, dp26_dt, dp27_dt, dp28_dt, dp29_dt, dp30_dt, dp31_dt]

@app.get("/")
async def main4(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/api/count")
async def count4(data  = Body()):
    try:
        t0 = data['p0']
        print(data)

        t_span = []

        t_start = 0
        t_end = data['t']
        dt = t_end/20

        t_now = t_start
        while (t_now < t_end):
            t_now = round(t_now,2)
            t_span.append(t_now)
            t_now = t_now + dt

        t_span.append(t_end)

        c = data['c']
        usolution,d = odeint(du4_dt, list(t0.values()), t_span, args=(c,), full_output=True)

        if (d["message"] != "Integration successful."):
            raise HTTPException(status_code=500)

        solution = [None] * len(usolution)
        idx = 0
        for elem in usolution:
            solution[idx] = list(elem)
            idx = idx + 1

        return JSONResponse(content={"solution": solution, "time": t_span})
    except:
        raise HTTPException(status_code=500)


