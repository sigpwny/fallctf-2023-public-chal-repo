<style>

</style>
<script>
    $: chat = [{ msg: "this music is goated", type: 'chat'} , {msg: "chat is this real", type: 'chat' }]
    let input = ''
    $: color = 'purple'
    $: watch = 'color'
    $: output = ''
    const sendInChat = async () => {
        if (input.length === 0) return
        const parts = input.split(' ')
        let is_cmd = false
        if (parts.length >= 2) {
            is_cmd = true
            const [cmd, ...bits] = parts
            const val = bits.join(' ')
            if (watch === 'color' && cmd === '/color') {
                setColor(val)
            } else if (watch === 'cow' && cmd === '/say') {
                try {
                    await askCowToSay(val)
                } catch {
                    output = 'Error!!'
                }
            } else if (cmd === '/watch') {
                watch = val
            } else {
                is_cmd = false
            }
        }
        
        
        chat = [...chat, { msg: input, type: is_cmd ? 'cmd' : 'chat' }]
        input = ''
    }

    const setColor = (val) => {
        color = val
    }

    const askCowToSay = async (val) => {
        const res = await fetch('/say', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: val }),
        })
        const resJSON = await res.json()
        output = resJSON.output || 'Error?'


    }
</script>
<div class="flex flex-row h-screen p-4">
    <div class="flex flex-col w-2/3 h-screen">
        {#if watch === 'color'}
        <div class="w-full h-2/3" style="background: {color}">
        </div>
        {:else if watch === 'cow'}
        <div class="w-full h-2/3 flex flex-col">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/rkR6b-zz-Rs?si=BU1t-2QW6nyfrMe2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            <pre><code>{output}</code></pre>
        </div>
        {:else}
        <div class="w-full h-2/3">
            i don't really want to watch {watch}
        </div>
        {/if}

        <div class="flex flex-row w-full h-1/3">
            <div class="w-20">
                <img class="object-scale-down rounded-full" alt="" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7be395c4-7285-48da-878f-c0d37c961840/d3ez8td-1b38f8b8-878e-43a6-8d88-f70ebcda1368.jpg/v1/fill/w_900,h_950,q_75,strp/shitty_charizard_by_grievousxxx_d3ez8td-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTUwIiwicGF0aCI6IlwvZlwvN2JlMzk1YzQtNzI4NS00OGRhLTg3OGYtYzBkMzdjOTYxODQwXC9kM2V6OHRkLTFiMzhmOGI4LTg3OGUtNDNhNi04ZDg4LWY3MGViY2RhMTM2OC5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.i-37QCiN51wBVSCad58-wEbjwaPgvFvlmfDS-KcEjYg">
            </div>
            <div class="flex flex-col flex-grow m-4">
                <div class="text-3xl">CarizardTV</div>
                <div class="flex flex-row justify-between">
                    {#if watch === 'cow'}
                        <div>COWCOWCOWCOWOCOWOCOW</div>
                    {:else}
                    <div>"{color.toUpperCase()}" - full 10 hour watch party</div>
                    {/if}
                    <div class="text-gray-800">9999 Viewers</div>
                </div>
            </div>
        </div>
    </div>
    <div class="outline-dashed w-1/3 flex flex-col justify-between">
        
        <div>

            {#each chat as msg}
                {#if msg.type === 'chat'}
                <div class="m-4 pl-2 outline-dotted">
                    {msg.msg}
                </div>
            {:else}
                <div class="m-4 pl-2 outline-dotted outline-blue-500">
                    {msg.msg}
                </div>
            {/if}
            {/each}
        </div>
        <div class="">
            <div class="m-4 outline outline-1">
                <form on:submit|preventDefault={sendInChat} class="flex flex-row">

                <input class="grow pl-2" type="text" placeholder="Send chat message" bind:value={input}>
                <button class="grow-0 pr-2" type="submit">ok</button>
                </form>
            </div>
        </div>
    </div>
</div>